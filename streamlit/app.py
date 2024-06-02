import streamlit as st
import keras
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import time
import os

current_directory = os.getcwd()

# Load the pre-trained model
model_path = os.path.join(current_directory, "cat_dog_clf_VGG16_production_model.h5")
# model_path = "cat_dog_classification_VGG16_2024_06_01__021235.keras"
model = load_model(model_path)
input_shape = (224, 224, 3)

# Set the page configuration
st.set_page_config(page_title="Cat-Dog Classifier", page_icon="🔎")

# Set and display the cover
cover_image_path = os.path.join(current_directory, "meow_or_woof.png")
cover_image = Image.open(cover_image_path)
st.image(cover_image, use_column_width=True)

# Add a header and description
st.header("Hello, my name is Classifier!")
st.divider()
st.write("I'm here to assist you to classify if it is a dog 🐶 or a cat 🐱!")

# Create a file uploader widget
uploaded_image = st.file_uploader(label="Click to upload image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    # Set the width and/or height parameters
    st.image(image, caption='Uploaded Image', width=300)  # Adjust width as needed
else:
    st.write("Please upload an image file.")

pred_but = st.button(label="Predict")

# Prediction Function
def predict_image_category(image, model, input_shape):
    img = image.resize(input_shape[:2])
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = tf.keras.applications.vgg16.preprocess_input(img_array)

    try:
        start_time = time.time()
        predictions = model.predict(img_array)
        end_time = time.time()
        prediction_time = end_time - start_time
        
        predicted_category = "Dog" if predictions[0][0] < predictions[0][1] else "Cat"
        confidence = max(predictions[0]) * 100
        result = "Predicted: {} ({:.2f}%), Time: {:.4f}s".format(
            predicted_category, confidence, prediction_time)
    except Exception as e:
        result = "Error predicting with model: {}".format(e)
    
    return result

if pred_but and uploaded_image is not None:
    results = predict_image_category(image, model, input_shape)
    st.success(results)
