import streamlit as st
import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root@123',
    database='weed_detector'
)
cursor = db.cursor()

def get_user_details(username):
    query = "SELECT email, mobile FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    return result if result else None

def profile(username):
    st.write('### Profile')
    user_details = get_user_details(username)

    if user_details:
        st.write(f"<span style='font-size: 30px;'>👩‍💼 Username : {username}</span>", unsafe_allow_html=True)
        st.write(f"<span style='font-size: 30px;'>📧 Email : {user_details[0]}</span>", unsafe_allow_html=True)
        st.write(f"<span style='font-size: 30px;'>📱 Mobile : {user_details[1]}</span>", unsafe_allow_html=True)
    else:
        st.write("User details not found.")
