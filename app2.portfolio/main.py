import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("")

with col2:
    st.title("Hrushikesh G")
    content = """
    Hi, I am Hrushikesh G! I am a python programmer and a student pursuing a Diploma in Computer Science at Dayananda Sagar Institute of Technology.
    I am doing this Python Certification to Master Python and become a Python Developer.
    """
    st.write(content)