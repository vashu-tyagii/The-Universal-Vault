"""
Topic: Input widgets — st.text_input, st.number_input, st.selectbox, 
st.slider, st.checkbox, st.radio, st.button
"""

import streamlit as st


# Input widgets let users enter values in the app.
# The value returned by a widget is stored in a Python variable.

st.title("Input Widgets")

# Text input: read a short piece of text.
name = st.text_input("What is your name?", placeholder="Enter your name")

# Number input: read a number.
age = st.number_input("How old are you?", min_value=0, max_value=120, step=1)

# Selectbox: choose one item from a list.
color = st.selectbox("Choose a color", ["Red", "Green", "Blue"])

# Slider: choose a value by moving a handle.
rating = st.slider("How do you rate this lesson?", 1, 10, 5)

# Checkbox: choose True (checked) or False (not checked).
likes_python = st.checkbox("I like Python")

# Radio: choose one item from a small list.
learning_level = st.radio("Choose your level", [
                          "Beginner", "Intermediate", "Advanced"])

# Button: run code when the button is clicked.
if st.button("Show my answers"):
    st.write(f"Name: {name or 'Not provided'}")
    st.write(f"Age: {age}")
    st.write(f"Color: {color}")
    st.write(f"Rating: {rating}/10")
    st.write(f"Likes Python: {'Yes' if likes_python else 'No'}")
    st.write(f"Level: {learning_level}")
