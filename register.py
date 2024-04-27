# register.py

import streamlit as st
import mysql.connector
from werkzeug.security import generate_password_hash

# Connect to MySQL database
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root@123',
    database='weed_detector'
)
cursor = db.cursor()

def register():
    st.write('### Register')
    new_username = st.text_input('👤 New Username')
    new_password = st.text_input('🔐 New Password', type='password')
    confirm_password = st.text_input('🔒 Confirm Password', type='password')
    email = st.text_input('📧 Email')
    mobile = st.text_input('📱 Mobile Number')
    
    if new_password != confirm_password:
        st.error('Passwords do not match. Please try again.')
    elif st.button('Register'):
        if create_user(new_username, new_password, email, mobile):
            st.success('Registration successful! Please login to continue.')
        else:
            st.error('Username already exists. Please choose a different username.')

def create_user(username, password, email, mobile):
    query = "INSERT INTO users (username, password, email, mobile) VALUES (%s, %s, %s, %s)"
    try:
        hashed_password = generate_password_hash(password)
        cursor.execute(query, (username, hashed_password, email, mobile))
        db.commit()
        return True
    except mysql.connector.Error as error:
        return False
