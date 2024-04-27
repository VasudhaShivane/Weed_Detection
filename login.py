# login.py

import streamlit as st
import mysql.connector
from werkzeug.security import check_password_hash

# Connect to MySQL database
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root@123',
    database='weed_detector'
)
cursor = db.cursor()

def login():
    st.write('### Login')
    username = st.text_input('👨‍💼 Username')
    password = st.text_input('🔒 Password', type='password')
    if st.button('Login'):
        if validate_login(username, password):
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.success('Login successful!')
            
        else:
            st.error('Invalid username or password')

def validate_login(username, password):
    query = "SELECT password FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    if result and check_password_hash(result[0], password):
        return True
    return False
