import streamlit as st
from PIL import Image

def run():
    # Add Picture
    image = Image.open('vtr.png')
    st.image(image, caption='Vehicle Type Recognition')
    # Title
    st.title('ABOUT THIS PROJECT')
    st.markdown('---')
    st.write('###### The main objective of this project is to build a machine learning model that can distinguish between four categories of vehicles: cars, trucks, buses, and motorcycles using Convolutional Neural Networks (CNN) and ElasticNet.')
    st.markdown('---')
    
    st.write('Feel free to contact me on:')
    st.write('[GITHUB](https://github.com/theonugraha)')
    st.write('or')
    st.write('[LINKEDIN](https://www.linkedin.com/in/nugrahatheo/)')


if __name__ == '__main__':
    run()