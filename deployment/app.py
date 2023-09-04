import streamlit as st
from streamlit_option_menu import option_menu
import recognition
import about

st.write('### VEHICLE TYPE RECOGNITION')
st.write('##### This page created by [Theo Nugraha](https://github.com/theonugraha)')
st.markdown('---')

selected = option_menu(None, ["About", "Recognition"], 
    icons=['house', 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "icon": {"color": "orange", "font-size": "15px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"1px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "grey"},
    }
)
    
selected
    

if selected == 'Recognition':
    recognition.run()
else:
    about.run()