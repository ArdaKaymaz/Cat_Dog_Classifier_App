import streamlit as st
import keras
import tensorflow as tf
from PIL import Image
import numpy as np
import os

model = tf.keras.models.load_model("streamlit/cat_dog_clf_model.h5")

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
    
    # Display the image with a caption
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Optionally, display additional information about the image
    # st.write(f"Image format: {image.format}")
    # st.write(f"Image size: {image.size}")
    # st.write(f"Image mode: {image.mode}")

else:
    st.write("Please upload an image file.")

pred_but = st.button(label="Predict")