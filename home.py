# home.py

import streamlit as st

def home():
    st.write('### Home')
    if getattr(st.session_state, 'logged_in', False):
        st.write(f"Logged in as: {st.session_state.username}")
       
        st.write("Welcome to the Weed Detection application. This tool helps in detecting weeds in agricultural crops using machine learning model.")

        st.write("---")

        st.write("### Actions")
        st.write("- **Upload Image**: Upload an image containing agricultural crops for weed detection.")
        st.write("- **View Weed Details**: View details about different types of weeds.")
        st.write("- **View User Profile**: View and edit your user profile.")
        
    else:
        st.write("Please login to view your profile.")
