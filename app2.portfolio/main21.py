import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/myphoto.jpg")

with col2:
    st.title("Hrushikesh G")
    content = """
    Hi, I am Hrushikesh G! I am a python programmer and a student pursuing a Diploma in Computer Science at Dayananda Sagar Institute of Technology.
    I am doing this Python Certification to Master Python and become a Python Developer.
    I am currently preparing for DCET 2026.
    I am aiming to finish my part of FSD Certification before 5th sem FSD subject.
    I am a Singer who is Learning Guitar.
    I also play Cricket and Football.
    """
    st.info(content)

content2 = """
Below you can find some of the apps i have built in Python.Feel free to contact me!
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
