# Application Developing Project with Generative AI

# 1 Streamlit Library

import streamlit as st

# 2 Start Streamlit

# st.write("Hello World")


# 3 Setting Page Configurations

st.set_page_config(page_title="Cat-Dog Classifier", page_icon="🔎")

st.header("Hello, my name is Classifier!")
st.divider()
st.write("I'm here to assist you to classify if it is a dog:dog2: or a cat:cat2:!")


# st.text_input(label="Your email:")
# st.text_input(label="Your password:", type="password")
# st.number_input(label="Your age", min_value=0, max_value=100, value=24)
# st.slider(label="Your age", min_value=0, max_value=100, value=24)
# st.checkbox(label="Remember me")
# st.radio(label="What is your status?", options=["student", "employed", "unemployed"])
# st.button(label="Login")
# st.file_uploader(label="Click to upload image")