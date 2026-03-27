# 🚗 Image Classification Model Project

## 📌 Introduction
We are a team from **Karpagam College of Engineering (AIDS Department)** called **Bit Rebels**.

We developed an **Image Classification Model** that classifies input images into **eight different classes**.

### 🔧 Technologies Used
- NumPy → Handles images as matrices  
- TensorFlow → Deep learning framework  
- Keras → High-level API within TensorFlow  

### 📂 Dataset Setup
- Dataset is split into:
  - Training set  
  - Testing set  
  - Validation set  
- Image dimensions (height & width) are predefined  

---

## 📊 Dataset Import and Preprocessing
- Dataset is loaded from the local directory  
- Images are shuffled to reduce overfitting  
- Defined parameters:
  - `image_size`
  - `batch_size`  
- `validation_split = False` (validation set already created)  
- Classes are automatically inferred  
- Additional datasets:
  - Test dataset  
  - Validation dataset  

---

## 🧠 Model Architecture

We use a **Sequential Deep Learning Model**.

### 🔹 Input Layer
- Rescales pixel values from **0–255 → 0–1**

### 🔹 Convolutional Layers
1. Conv Layer 1
   - 16 filters  
   - Kernel size: 3×3  
   - Padding: `same`  
   - Activation: ReLU  

2. Conv Layer 2
   - 32 filters  
   - Same configuration  

3. Conv Layer 3
   - 64 filters  

### 🔹 Pooling Layers
- MaxPooling2D after each convolution layer  

### 🔹 Fully Connected Layers
- Flatten Layer → Converts 2D → 1D  
- Dropout (0.2) → Prevents overfitting  
- Dense Layer (128 neurons)  
- Output Layer → 8 classes  

---

## ⚙️ Training Configuration
- Optimizer: Adam  
- Loss Function: `from_logits=True`  
- Metric: Accuracy  

### 🏋️ Training Details
- Epochs: 25  
- Uses training and validation datasets  

---

## 🔍 Prediction Workflow
1. Load image  
2. Convert to array  
3. Expand dimensions  
4. Model outputs 8 raw scores  
5. Apply Softmax  
6. Use `np.argmax`  
7. Display predicted class and confidence score  

---

## 📈 Evaluation Metrics and Threshold

### 📊 Metrics Used
- Accuracy  
- Precision (Macro Average)  
- Classification Report  

### 🎯 Confidence Threshold: 0.80

#### 💡 Justification
- >0.80 → Rejects correct predictions  
- <0.80 → Accepts weak predictions  

**0.80 provides the best balance between reliability and usability.**

---

## 🚀 Conclusion
This project demonstrates a robust **CNN-based Image Classification System** with:
- Efficient preprocessing  
- Strong architecture  
- Balanced evaluation  
- Reliable predictions  
