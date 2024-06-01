import streamlit as st
import keras
import tensorflow as tf
from PIL import Image
import numpy as np
import os
import time

model = tf.keras.models.load_model("cat_dog_classification_VGG16_2024_06_01__021235.keras")
input_shape = (224, 224, 3)

# Set the page configuration
st.set_page_config(page_title="Cat-Dog Classifier", page_icon="🔎")

# Add a header and description
st.header("Hello, my name is Classifier!")
st.divider()
st.write("I'm here to assist you to classify if it is a dog 🐶 or a cat 🐱!")

# Create a file uploader widget
uploaded_image = st.file_uploader(label="Click to upload image", type=["jpg", "jpeg", "png"])


if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)


else:
    st.write("Please upload an image file.")


pred_but = st.button(label="Predict")

# Prediction Function
def predict_image_category(image_path, model, input_shape):
    img = keras.preprocessing.image.load_img(
        image_path, target_size=input_shape[:2]
    )
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    results = []
    try:
        start_time = time.time()
        predictions = model.predict(img_array)
        end_time = time.time()
        prediction_time = end_time - start_time
        
        predicted_category = "Dog" if predictions[0][0] < predictions[0][1] else "Cat"
        confidence = max(predictions[0]) * 100
        results.append("Model: {}, Predicted: {} ({:.2f}%), Time: {:.4f}s".format(
            model, predicted_category, confidence, prediction_time))
    except Exception as e:
        results.append("Error predicting with model {}: {}".format(model, e))
    
    return print(results)


if pred_but:
    results = predict_image_category(uploaded_image, model, input_shape)
    st.write(results)