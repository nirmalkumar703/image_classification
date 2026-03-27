🚗 Image Classification Model Project
📌 Introduction

We are a team from Karpagam College of Engineering (AIDS Department) called Bit Rebels.

We developed an Image Classification Model that classifies input images into eight different classes.

🔧 Technologies Used
NumPy → Handles images as matrices
TensorFlow → Deep learning framework
Keras → High-level API within TensorFlow
📂 Dataset Setup
Dataset is split into:
Training set
Testing set
Validation set
Image dimensions (height & width) are predefined
📊 Dataset Import and Preprocessing
Dataset is loaded from the local directory
Images are shuffled to reduce overfitting
Defined parameters:
image_size
batch_size (number of images processed at once)
validation_split = False (since validation set is already separate)
Classes are automatically inferred
Additional datasets:
Test dataset
Validation dataset
🧠 Model Architecture

We use a Sequential Deep Learning Model.

🔹 Input Layer
Rescales pixel values from 0–255 → 0–1
🔹 Convolutional Layers
Conv Layer 1
16 filters
Kernel size: 3×3
Padding: same
Activation: ReLU
Conv Layer 2
32 filters
Same configuration
Learns deeper features
Conv Layer 3
64 filters
Extracts high-level features
🔹 Pooling Layers
MaxPooling2D used after each convolution layer
Reduces spatial dimensions while keeping key features
🔹 Fully Connected Layers
Flatten Layer → Converts 2D → 1D
Dropout Layer (0.2) → Prevents overfitting
Dense Layer (128 neurons) → Feature combination
Output Layer → 8-class prediction
⚙️ Training Configuration
Optimizer: Adam
Loss Function:
Uses from_logits=True
Because output is raw values (not probabilities)
Metric: Accuracy
🏋️ Training Details
Epochs: 25
Uses:
Training dataset
Validation dataset
🔍 Prediction Workflow
Load image
Convert to array
Expand dimensions (batch format)
Model outputs 8 raw scores
Apply Softmax → Convert to probabilities
Use np.argmax → Get predicted class
Display:
Predicted class
Confidence score
📈 Evaluation Metrics and Threshold
📊 Evaluation Process
Use unseen test dataset
Combine features into NumPy arrays
Generate predictions
📏 Metrics Used
Accuracy
Precision (Macro Average for multi-class)
Classification Report (per-class metrics)
🎯 Confidence Threshold Strategy
Model outputs are probabilities but not perfectly calibrated
Observed confidence range: 0.75 – 0.85
✅ Selected Threshold: 0.80
💡 Justification
Higher (>0.80):
Rejects many correct predictions ❌
Lower (<0.80):
Accepts weak predictions ❌

👉 0.80 provides the best balance

Improves reliability
Maintains usability
Enhances overall system trust
🚀 Conclusion

This project demonstrates a robust Deep Learning-based Image Classification System with:

Efficient preprocessing
Well-structured CNN architecture
Balanced evaluation strategy
Reliable prediction threshold
