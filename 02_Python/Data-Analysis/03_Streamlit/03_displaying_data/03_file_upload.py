"""
Topic: Upload and display a CSV file

Notes:
- st.file_uploader() lets the user choose a file.
- pd.read_csv() reads the uploaded CSV into a DataFrame.
- st.dataframe() displays the DataFrame in the app.

Run with:
	streamlit run 03_file_upload.py
"""

import pandas as pd
import streamlit as st


st.title("CSV File Viewer")

# Ask the user to choose a CSV file.
uploaded_file = st.file_uploader(
    "Choose a CSV, JSON, or Excel file",
    type=["csv", "json", "xlsx", "xls"],
)

if uploaded_file is not None:
    # Read the uploaded file into a Pandas DataFrame.
    file_extension = uploaded_file.name.rsplit(".", 1)[-1].lower()
    if file_extension == "csv":
        data = pd.read_csv(uploaded_file)
    elif file_extension == "json":
        data = pd.read_json(uploaded_file)
    else:
        data = pd.read_excel(uploaded_file) # type: ignore

    st.subheader("Uploaded data")
    st.dataframe(data)  # type: ignore
else:
    st.info("Please upload a CSV file to see its data.")
