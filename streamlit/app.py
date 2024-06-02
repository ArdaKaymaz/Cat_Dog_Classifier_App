import streamlit as st

st.set_page_config(page_title="Cat-Dog Classifier", page_icon=":paw_prints:")

import keras
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import time
import os

current_directory = os.getcwd()

@st.cache_resource
def load_model_cached(model_path):
    return load_model(model_path)

model_path = os.path.join(current_directory, "cat_dog_clf_VGG16_production_model.h5")
model = load_model_cached(model_path)
input_shape = (224, 224, 3)

cover_image_path = os.path.join(current_directory, "meow_or_woof.png")
cover_image = Image.open(cover_image_path)
st.image(cover_image, use_column_width=True)

st.header("Hello, my name is Cat-Dog Classifier!")
st.divider()
st.write("I'm here to clear up the confusion about whether your pet is a cat 🐱 or a dog 🐶!")

tab1, tab2 = st.tabs(["Application", "About"])

with tab1:

    st.write("Please upload an image and press 'Predict' button")

    uploaded_image = st.file_uploader(label="Click to upload image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image', width=300)
    else:
        st.write("Please upload an image file.")

    pred_but = st.button(label="Predict")

    def predict_image_category(image, model, input_shape):
        img = image.resize(input_shape[:2])
        img_array = keras.preprocessing.image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
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

with tab2:

    st.header("About the App")

    st.subheader("Development Process")

    st.write("The project involves the development and deployment of an image classification application using Streamlit, \
             an open-source app framework. The application leverages three prominent convolutional neural network (CNN) \
             architectures: MobileNet, VGG16, and ResNet50, with VGG16 ultimately chosen for production. The development \
             process was tracked and managed using MLflow, and the models were trained using TensorFlow and Keras libraries.")
