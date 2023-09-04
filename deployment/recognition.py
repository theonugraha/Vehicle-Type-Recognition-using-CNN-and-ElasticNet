# Import library
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import pickle
import json
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input
  
def predict_and_display(uploaded_file, model, class_labels):
    img = Image.open(uploaded_file)
    img = img.resize((224, 224))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    prediction = model.predict(img_array)
    predicted_class_index = np.argmax(prediction)
    predicted_class_label = class_labels[predicted_class_index]

    st.image(img, use_column_width=True)
    st.write(f"Predicted Vehicle: {predicted_class_label}")

def run():
    st.write('##### Form Upload Vehicle Type Recognition')
    # Making Form
    # Create a Streamlit form
    with st.form(key='Form Upload Vehicle Type Recognition'):
        # Add a file uploader to the form
        uploaded_files = st.file_uploader("Choose a .JPEG/.JPG/.PNG file", accept_multiple_files=True)

        # Check if any file is uploaded
        if uploaded_files:
            for uploaded_file in uploaded_files:
                st.write("filename:", uploaded_file.name)

                # Load trained model
                model = load_model('model_fix.h5')

                # Define class labels
                class_labels = ['Bus', 'Car', 'Truck', 'Motorcycle']

                # Use the predict_and_display function with the uploaded image data
                predict_and_display(uploaded_file, model, class_labels)

        # Close the form
        st.form_submit_button(label='Submit')
        
if __name__ == '__main__':
    run()