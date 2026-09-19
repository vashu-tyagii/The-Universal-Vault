"""
Topic: Apply everything so far to a real dataset — load one of your CSVs 
(Palin/Dropout/Retail), add a filter widget (e.g. selectbox for Course/Region), 
and show the filtered DataFrame
"""

"""A simple dashboard for loading and filtering a real CSV file."""

import pandas as pd
import streamlit as st


# Add a title and a short instruction.
st.title("Load and Filter Real Data")
st.write("Upload a CSV file and choose a value to filter the data.")

# The file can be a Palin, Dropout, or Retail CSV file.
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
	# Read the CSV file into a pandas DataFrame.
	data = pd.read_csv(uploaded_file)

	st.subheader("Original data")
	st.dataframe(data)  # type: ignore

	# Prefer Course or Region when one of those columns exists.
	preferred_columns = [
		column for column in ("Course", "Region") if column in data.columns
	]
	filter_column = st.selectbox(
		"Choose a column to filter",
		preferred_columns or list(data.columns),
	)

	# Make a list of the unique values in the selected column.
	values = data[filter_column].dropna().unique().tolist()
	selected_value = st.selectbox("Choose a value", ["All"] + values)

	# Keep all rows or only rows matching the selected value.
	if selected_value == "All":
		filtered_data = data
	else:
		filtered_data = data[data[filter_column] == selected_value]

	st.subheader("Filtered data")
	st.write(f"Rows found: {len(filtered_data)}")
	st.dataframe(filtered_data) # type: ignore
else:
	st.info("Upload a CSV file to begin.")
