# 📊 SIAMESE NN PERFORMANCES: NUMBER RECOGNITION
  
## 💬 FULL-DISCLOSURE:
### ⚠️ MODEL'S LIMITATIONS
Since this is an embryonic phase of a more ambitious project, the network was trained on the MNIST dataset alone. As a result, the model is used to deal ONLY with white-digits ⚪️ on a black-background ⚫️ pics. Therefore, any image uploaded for comparison must  
- *a)* be a number 🔢
- *b)* be "regularized" into a black-background-white-digit layout ⚫️⚪️  

Depending on the the original image's scale, pixel quality and colors, the pre-processing (i.e regularization) step may vary in difficulty. The greater the effort required in this process, the higher the risk for the network to mistakenly identify the digits❌.

### 🚀 MODEL'S ENHANCEMENTS
As bad as limits are, acknowledging them is key, as it means understanding what should be tweaked to improve model's performance. In details, three main directions can significantly enhance the model's performances:
  
- 1️⃣ The most classic one: fine-tuning the network's parameters. At this stage, only a subset of parameters has been tuned. Further calibration (e.g., learning rate, margin, optimizer settings) can improve embedding quality and similarity discrimination.  
- 2️⃣ Expanding the training pool by adding images with different layouts. Colored background and digits plus various contrast will teach the model to handle unseen conditions, boosting the model generalization and robustness.  
- 3️⃣ Improving Normalizazion or pre-processing. As the dataset grows in diversity, the current regularization process may be replaced or supplemented by a standardized normalization pipeline to ensure consistency across inputs.
  
  

## 📈 PERFORMANCES EXAMPLES: THE GOODs AND THE BADs
### ✅ THE GOODs
 
_________________________________________________________________________________________________________________________________

<img width="895" height="400" alt="7-ok" src="https://github.com/user-attachments/assets/e81db63f-c060-4913-8575-a967a267f062" />
  
_________________________________________________________________________________________________________________________________

<img width="905" height="432" alt="8-ok" src="https://github.com/user-attachments/assets/dac2238c-9514-414a-9fc6-78fe92793b2a" />
  
_________________________________________________________________________________________________________________________________

<img width="910" height="448" alt="9-ok" src="https://github.com/user-attachments/assets/0bd364f5-c1ef-4fcd-9bf4-da7768423e69" />
  
_________________________________________________________________________________________________________________________________

<img width="898" height="415" alt="6-ok" src="https://github.com/user-attachments/assets/42a0fb1f-efaa-42a8-8d39-4dd5f07373a2" />

_________________________________________________________________________________________________________________________________
### ❌ THE BADs
  
_________________________________________________________________________________________________________________________________

<img width="902" height="402" alt="7-wrong" src="https://github.com/user-attachments/assets/bb9fa5b9-3e1b-4b3c-a9a5-b779324b156d" />
  
_________________________________________________________________________________________________________________________________

<img width="884" height="431" alt="1-wrong" src="https://github.com/user-attachments/assets/791280ba-2290-4e47-9c33-bf8c4cd0bede" />
  
_________________________________________________________________________________________________________________________________

