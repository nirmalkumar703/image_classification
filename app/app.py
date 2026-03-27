# from flask import Flask, request, jsonify
# from werkzeug.utils import secure_filename
# import os
# from flask_cors import CORS

# app = Flask(__name__)

# # ✅ Allow all origins (for development)
# CORS(app, resources={r"/*": {"origins": "*"}})


# # Folder to store uploaded images
# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Create folder if not exists
# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)


# @app.route('/upload', methods=['POST'])
# def upload_image():
#     try:
#         # 1. Check if file is present
#         if 'image' not in request.files:
#             return jsonify({
#                 "status": "error",
#                 "message": "No image file provided"
#             }), 400

#         file = request.files['image']

#         # 2. Check if filename is empty
#         if file.filename == '':
#             return jsonify({
#                 "status": "error",
#                 "message": "No file selected"
#             }), 400

#         # 3. Secure filename and save
#         filename = secure_filename(file.filename)
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(file_path)

#         # 4. Success response
#         return jsonify({
#             "status": "success",
#             "message": "input received"
#         }), 200

#     except Exception as e:
#         # 5. Exception handling
#         return jsonify({
#             "status": "error",
#             "message": "Something went wrong",
#             "error": str(e)
#         }), 500


# # Run server
# if __name__ == '__main__':
#     app.run(debug=True)/




# import tensorflow as tf
# from tensorflow.keras.models import load_model
# from tensorflow.keras.layers import Dense
# from flask import Flask, request, jsonify
# from werkzeug.utils import secure_filename
# import os
# from flask_cors import CORS
# import numpy as np
# import cv2

# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "*"}})

# # 📁 Upload folder
# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)

# # ==============================
# # 🧠 Load Keras model (.h5) safely
# # ==============================

# # Custom Dense class to ignore 'quantization_config'
# class DenseIgnore(Dense):
#     def __init__(self, *args, **kwargs):
#         kwargs.pop("quantization_config", None)  # Remove it if exists
#         super().__init__(*args, **kwargs)

# model = load_model("image_classify.keras", compile=False, custom_objects={"Dense": DenseIgnore})
# print("✅ Keras model loaded successfully")

# # ⚠️ Update according to your model input size
# IMG_SIZE = 224
# data_cat=['Auto Rickshaws', 'Bikes','Cars' , 'Motorcycles', 'Planes', 'Ships', 'Trains']

# @app.route('/upload', methods=['POST'])
# def upload_image():
#     try:
#         if 'image' not in request.files:
#             return jsonify({"status": "error", "message": "No image file provided"}), 400

#         file = request.files['image']
#         if file.filename == '':
#             return jsonify({"status": "error", "message": "No file selected"}), 400

#         filename = secure_filename(file.filename)
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(file_path)

#         # ==============================
#         # 🖼 Preprocess Image
#         # ==============================
#         img = cv2.imread(file_path)
#         if img is None:
#             return jsonify({"status": "error", "message": "Invalid image file"}), 400

#         img = cv2.resize(img, (180, 180))
#         img = img / 255.0
#         img = np.expand_dims(img, axis=0)

#         # ==============================
#         # 🎯 Prediction
#         # ==============================
#         prediction = model.predict(img)

#         # 👉 Binary classification (edit if multi-class)
#         result = int(prediction[0][0] > 0.5)
#         confidence = float(prediction[0][0])

# #         image = r"C:/Users/Kanis/Downloads/AI batch hackthon/ship_images.jpg"
#         image = tf.keras.utils.load_img(file_path, target_size=(180,180))
#         img_arr = tf.keras.utils.array_to_img(image)
#         img_bat=tf.expand_dims(img_arr,0)
#         predict = model.predict(img_bat)
#         score = tf.nn.softmax(predict)
#         output='veichle in image is {} with accuracy of {:0.2f}'.format(data_cat[np.argmax(score)],np.max(score)*100)
#         print(output)

#         return jsonify({
#             "status": output,
#             "message": "input received",
#             "prediction": result,
#             "confidence": round(confidence, 4)
#         }), 200

#     except Exception as e:
#         return jsonify({
#             "status": "error",
#             "message": "Something went wrong",
#             "error": str(e)
#         }), 500

# # Run server
# if __name__ == '__main__':
#     app.run(debug=True)

#import tensorflow as tf
#print(tf.__version__)


import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Dense
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from flask_cors import CORS
import numpy as np
import cv2

# ==============================
# Flask setup
# ==============================
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ==============================
# Custom Dense to ignore quantization_config
# ==============================
# class DenseIgnore(Dense):
#     def __init__(self, *args, **kwargs):
#         kwargs.pop("quantization_config", None)
#         super().__init__(*args, **kwargs)






# ==============================
# Load .keras model
# ==============================
#model = load_model("veichal_classification_model.keras", compile=False, custom_objects={"Dense": DenseIgnore})

# import tensorflow as tf

# def load_compatible_model(path):
#     return tf.keras.models.load_model(
#         path,
#         compile=False,
#         custom_objects={
#             "InputLayer": tf.keras.layers.InputLayer
#         }
#     )

model = load_model(r'hackthon_image_classification_model.keras')
#model = load_model('C:\Users\Kanis\Downloads\AI_batch_hackthon\veichal_classification_model.keras')
print("✅ Model loaded successfully")
# model = load_model(
#     "veichal_classification_model.h5",
#     compile=False,
#     custom_objects={"InputLayer": tf.keras.layers.InputLayer}
# )
# print("✅ Model loaded successfully")

# ==============================
# Model input size
# ==============================
IMG_SIZE = 180  # Must match your model input
data_cat = ['Ambulances',
 'Auto Rickshaws',
 'Bikes',
 'Cars',
 'Motorcycles',
 'Planes',
 'Ships',
 'Trains']

# ==============================
# Flask route
# ==============================
@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        if 'image' not in request.files:
            return jsonify({"status": "error", "message": "No image file provided"}), 400

        file = request.files['image']
        if file.filename == '':
            return jsonify({"status": "error", "message": "No file selected"}), 400

        # Save uploaded image
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # ==============================
        # Preprocess image
        # ==============================

       # image = r"C:/Users/Kanis/Downloads/AI_batch_hackthon/ship_images.jpg"
        image = tf.keras.utils.load_img(file_path, target_size=(180,180))

        if not image:
            return jsonify({"status": "error", "message": "Invalid image file"}), 400

        img_arr = tf.keras.utils.img_to_array(image)
        img_bat=tf.expand_dims(img_arr,0)

        predict = model.predict(img_bat)

        score = tf.nn.softmax(predict)

        output=data_cat[np.argmax(score)]

        print(output)
        score=np.max(score)*100
        print(score)

        if score >= 80:
            decision = "High Confidence Classification"
        elif score >= 60:
            decision = "Ambiguous / Needs Review"
        else:
            decision = "Uncertain Prediction"

        print(decision)

        
        

        #img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
        #img = img / 255.0
        #img = np.expand_dims(img.astype(np.float32), axis=0)  # Shape: (1, IMG_SIZE, IMG_SIZE, 3)

        # ==============================
        # Predict
        # ==============================
       # preds = model.predict(img)
       # score = tf.nn.softmax(preds[0])
       ## class_idx = int(np.argmax(score))
        #confidence = float(np.max(score))

        #output = f"Vehicle in image is '{data_cat[class_idx]}' with accuracy of {confidence*100:.2f}%"
       # print(output)

        return jsonify({
            "status": "success",
            "message": decision,
            "prediction": output,
            "confidence": score
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "Something went wrong",
            "error": str(e)
        }), 500

# ==============================
# Run server
# ==============================
if __name__ == '__main__':
    app.run(debug=True)