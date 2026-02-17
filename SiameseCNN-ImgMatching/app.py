import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import gradio as gr
from PIL import Image, ImageOps
from torchvision.datasets import MNIST
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
from scipy.ndimage import shift

# ---------------- MODEL ----------------

class SiameseNetworkBatch(nn.Module):
    def __init__(self):
        super().__init__()

        self.cnn = nn.Sequential(
            nn.Conv2d(1, 64, 5, 1, 2),
            nn.BatchNorm2d(64),
            nn.ReLU(True),
            nn.MaxPool2d(2),

            nn.Conv2d(64, 128, 5, 1, 2),
            nn.BatchNorm2d(128),
            nn.ReLU(True),
            nn.MaxPool2d(2),

            nn.Conv2d(128, 256, 3, 1, 1),
            nn.BatchNorm2d(256),
            nn.ReLU(True),
            nn.MaxPool2d(2)
        )

        self.fc = nn.Sequential(
            nn.Linear(256 * 3 * 3, 1024),
            nn.ReLU(True),
            nn.Linear(1024, 256),
            nn.ReLU(True),
            nn.Linear(256, 2)
        )

    def forward_once(self, x):
        out = self.cnn(x)
        out = out.view(out.size(0), -1)
        return self.fc(out)


# ---------------- LOAD MODEL ----------------

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = SiameseNetworkBatch().to(device)
model.load_state_dict(torch.load("Siamese_model.pt", map_location=device))
model.eval()

transform = transforms.ToTensor()

# ---------------- LOAD MNIST ----------------

data_tt = MNIST(root="./data", train=False, download=True)

test_imgs = []
test_labels = []
test_embeds = []

print("Precomputing MNIST embeddings...")

with torch.no_grad():
    for img, label in data_tt:
        img_tensor = transform(img).unsqueeze(0).to(device)
        emb = model.forward_once(img_tensor)

        test_imgs.append(img)
        test_labels.append(label)
        test_embeds.append(emb)

print("Done!")

# ---------------- PREDICTION ----------------

def preprocess_user_image(img):
    # Convert to grayscale
    img = img.convert("L")

    # Invert if background is white
    if np.mean(np.array(img)) > 127:
        img = ImageOps.invert(img)

    img_np = np.array(img)

    # ---- 1. Binarize ----
    img_np = (img_np > 30).astype(np.uint8) * 255

    # ---- 2. Find bounding box ----
    coords = np.column_stack(np.where(img_np > 0))

    if len(coords) == 0:
        return Image.fromarray(np.zeros((28, 28), dtype=np.uint8))

    y_min, x_min = coords.min(axis=0)
    y_max, x_max = coords.max(axis=0)

    digit = img_np[y_min:y_max+1, x_min:x_max+1]

    # ---- 3. Resize longest side to 20 px ----
    h, w = digit.shape

    if h > w:
        new_h = 20
        new_w = int(w * (20 / h))
    else:
        new_w = 20
        new_h = int(h * (20 / w))

    digit = Image.fromarray(digit).resize((new_w, new_h), Image.LANCZOS)

    digit_np = np.array(digit)

    # ---- 4. Pad to 28x28 ----
    padded = np.zeros((28, 28), dtype=np.uint8)

    y_offset = (28 - new_h) // 2
    x_offset = (28 - new_w) // 2

    padded[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = digit_np

    # ---- 5. Center using center of mass ----
    coords = np.column_stack(np.where(padded > 0))
    cy, cx = coords.mean(axis=0)

    shift_y = int(14 - cy)
    shift_x = int(14 - cx)

    from scipy.ndimage import shift
    padded = shift(padded, shift=(shift_y, shift_x), mode='constant')

    return Image.fromarray(padded.astype(np.uint8))



def predict(img):

    try:

        # ---------------- SAFE INPUT HANDLING ----------------
    
        if img is None:
            return "Please draw or upload an image", None

        # If Sketchpad dict
        if isinstance(img, dict):
        
            # Try composite first
            if "composite" in img and img["composite"] is not None:
                img = img["composite"]
        
            # Otherwise try layers
            elif "layers" in img and len(img["layers"]) > 0:
                img = img["layers"][0]
        
            else:
                return "Please draw something first", None
        
        # Convert numpy to PIL
        if isinstance(img, np.ndarray):
        
            if img.max() <= 1.0:
                img = (img * 255).astype(np.uint8)
        
            # Remove alpha channel if exists
            if len(img.shape) == 3 and img.shape[2] == 4:
                img = img[:, :, :3]
        
            img = Image.fromarray(img)
        
        # Final validation
        if not isinstance(img, Image.Image):
            return "Invalid image format", None
        
        img = img.convert("L")
    
        # ---------------- PREPROCESS ----------------
        img = preprocess_user_image(img)
    
        img_tensor = transform(img).unsqueeze(0).to(device)
    
        # ---------------- EMBEDDING ----------------
        with torch.no_grad():
            user_embed = model.forward_once(img_tensor)
    
        distances = [
            F.pairwise_distance(user_embed, e).item()
            for e in test_embeds
        ]
    
        top3_idx = np.argsort(distances)[:3]
    
        results = []
        fig, axes = plt.subplots(1, 4, figsize=(10, 3))
    
        axes[0].imshow(img, cmap="gray")
        axes[0].set_title("Your drawing")
        axes[0].axis("off")
    
        for i, idx in enumerate(top3_idx):
            match_img = test_imgs[idx]
            label = test_labels[idx]
            sim = np.exp(-distances[idx])
    
            axes[i+1].imshow(match_img, cmap="gray")
            axes[i+1].set_title(f"{label}\nSim {sim:.3f}")
            axes[i+1].axis("off")
    
            results.append((label, sim))

        plt.tight_layout()
    
        best_label = results[0][0]
    
        return f"Predicted digit: {best_label}", fig

    except Exception as e:
        
        import traceback
        traceback.print_exc()
        return f"Error: {str(e)}", None



# ---------------- UI ----------------

with gr.Blocks(title="Siamese MNIST Matcher") as demo:

    gr.Markdown("# Siamese MNIST Matcher")
    gr.Markdown("Draw or upload a digit. The model shows the 3 most similar MNIST images.")

    with gr.Tabs():

        # -------- DRAW TAB --------
        with gr.Tab("Draw digit"):
            draw_input = gr.Sketchpad(
                label="Draw a digit",
                height=280,
                width=280,
            )

            draw_btn = gr.Button("Predict")
            draw_text = gr.Textbox(label="Prediction")
            draw_plot = gr.Plot(label="Top 3 matches")

            draw_btn.click(
                fn=predict,
                inputs=draw_input,
                outputs=[draw_text, draw_plot]
            )

        # -------- UPLOAD TAB --------
        with gr.Tab("Upload image"):
            upload_input = gr.Image(type="pil", label="Upload digit image")
            upload_btn = gr.Button("Predict")
            upload_text = gr.Textbox(label="Prediction")
            upload_plot = gr.Plot(label="Top 3 matches")

            upload_btn.click(
                fn=predict,
                inputs=upload_input,
                outputs=[upload_text, upload_plot]
            )


demo.launch()