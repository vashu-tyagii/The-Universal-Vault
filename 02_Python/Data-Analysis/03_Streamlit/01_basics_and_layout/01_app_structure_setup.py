"""
Topic: Basic Streamlit app structure

Run this file in a terminal with:
	streamlit run 01_app_structure_setup.py

Streamlit displays the Python code as a web page.
"""

import streamlit as st


# Configure the browser tab title and page layout.
st.set_page_config(page_title="My First Streamlit App",
                   page_icon="🔐", layout="centered")

# st.title() adds the main title.
st.title("My First Streamlit App")

# st.header() adds a section heading.
st.header("Welcome")

# st.write() displays text, numbers, and Python objects.
st.write("This page was created with Python and Streamlit.")
st.write("2 + 3 =", 2 + 3)

# st.text() displays simple plain text.
st.text("This is plain text.")

# Save the file and run the command in the note above to view the app.
