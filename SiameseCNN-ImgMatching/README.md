# 🔢 Siamese CNN: Number Recognition & Similarities
📩
<a href="mailto:lucagabri98@live.it"><img src="https://img.shields.io/badge/lucagabri98-c71610?style=flat&logo=gmail&logoColor=white" width="80"></a>
<a href="la-databizanalyst"><img src="https://img.shields.io/badge/%40LA-0E76A8?style=flat&logo=linkedin&logoColor=white" width="32"></a>
📩  

**🎯Try out the model [here](https://huggingface.co/spaces/Lullooo/SiameseCNN-ImgMatching)**
**Note:** See model performances and examples [here 📈](https://github.com/Lulloooo/SiameseNet-NumRecognition/blob/main/Performances-Examples.md)
<br/><br/>
## 🎯 PURPOSES
This project aims to develop a Siamese Neural Network 🧠 able to match and identify different kinds of numerical digits 🔢.  
The model learns to measure how similar two images are rather than directly classifying them. This makes it suitable for tasks like:  

- **🤝 Digits matching and recognition**: Compare the uploaded digits with those in the test set. Once a match is found, label the uploaded digit with the same label as the matched one.
- **🔓 Security unlocking mechanisms**: The camera captures an istant image of a face or an object. If the similarity with those in the training pool is high, it unlocks the device/program.
- **🔎 Duplicate detection**: Define a similarity score between the external image and those in the reference set. If similarity with one of these is high, it is likely is a duplicate.
<br/><br/>
## 🛠️ WORKFLOW
The workflow is quite straightforward: the user is prompted to upload a picture of a number, and the Siamese Network returns:  
- 1️⃣ The black-background and white digit version of the picture  
- 2️⃣ A matching pic coming from the testing dataset along with its similarity score  
- 3️⃣ Which digit is the uploaded picture (The uploaded img is a ...)
<br/><br/>
## ⚠️ WARNINGS 
Be sure to run the program on GPU 🤖, as this is needed for the Siamese CNN to work properly.  
Plus, be fully aware of the model's limitations by reading the [model limitations doc ✋](https://github.com/Lulloooo/SiameseNet-NumRecognition/blob/main/Performances-Examples.md)
<br/><br/>
## 🧠 MODEL OVERVIEW  
The Siamese architecture leverages shared convolutional layers to extract features from two images, then computes their Euclidean distance in embedding space. A contrastive loss function is employed:

&nbsp;&nbsp;**L = (1 - Y) * (1/2) * D^2 + Y * (1/2) * (max(0, m - D))^2**

with:
- D: distance between embeddings
- Y = 0 for similar and Y = 1 for dissimilar
- m: margin parameters (can be changed)
<br/><br/>
## 🗂️ REPO'S DESCRIPTION
This folder contains the material for the early phase of a more ambitious security unlocking mechanism project. It was a first-stage project, fine-tuned later, designed to develop a procedure that unblocks  programs only after an image match is found.  
In details, this repo contains (other than this ReadMe):  
- 1️⃣ **Siamese_TrainAndEvaluation.ipynb**: Main notebook for model definition, training, and performance visualization.
- 2️⃣ **Siamese_predict.ipynb**: Notebook for prediction and visual similarity inference on new samples. This is the notebook that the user testing the model must run.
- 3️⃣ **Siamese_model.pt**: Final trained model weights.
- 4️⃣ **Tuning_siamese_model.pt**: Tuned model version before the final re-training on the full training dataset.  
- 5️⃣ **Performances-Examples.md**: Discussion about model performances, limitations and possible enhancements. Visual examples are included.
<br/><br/>
## 📪 GET IN TOUCH
<a href="mailto:lucagabri98@live.it"><img src="https://img.shields.io/badge/lucagabri98-c71610?style=flat&logo=gmail&logoColor=white" width="80"></a>
<a href="la-databizanalyst"><img src="https://img.shields.io/badge/%40LA-0E76A8?style=flat&logo=linkedin&logoColor=white" width="32"></a>  
Feel free to reach out to point out issues and/or suggest improvements. I'll be happy to chat about it and implement them. 💬   
  
__________________________________________________________________________________________________________
**Note**: I got the idea to implement this kind of network for this kind of task + some code chunks from the [Daily Dose of Data Science](https://www.dailydoseofds.com/) newsletter 📨. They are really awesome, and everyone interested in data science should check them too 😉.  
  

**Note2**: As this was a work-related project, it has been approved for posting, and all sensitive information and data are omitted to protect privacy. Code snippet containing sensitive data has not been posted. 
__________________________________________________________________________________________________________
