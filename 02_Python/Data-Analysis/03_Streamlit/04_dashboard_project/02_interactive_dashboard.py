"""
Topic: Build a small interactive dashboard.

Notes:
1. Upload a CSV file, or use the small example data.
2. Choose a column to filter.
3. View simple metrics and a chart.

Run this file with:
	streamlit run 02_interactive_dashboard.py
"""

import pandas as pd
import streamlit as st


# Page title and a short introduction.
st.title("Simple Interactive Dashboard")
st.write("Upload a CSV file or explore the example data below.")


# A file uploader lets us use a real dataset.
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
else:
    # Example data keeps the dashboard useful while no file is uploaded.
    data = pd.DataFrame(
        {
            "Category": ["A", "A", "B", "B", "C"],
            "Sales": [120, 180, 90, 140, 210],
        }
    )


st.subheader("Data preview")
st.dataframe(data.head()) # type: ignore

# Find numeric columns so the metrics and chart work with many datasets.
numeric_columns = data.select_dtypes(include="number").columns.tolist()

if not numeric_columns:
    st.warning("This dataset has no numeric columns to display.")
else:
    number_column = st.selectbox("Choose a numeric column", numeric_columns)

    # A filter widget is shown when the dataset has text or category columns.
    category_columns = data.select_dtypes(exclude="number").columns.tolist()
    if category_columns:
        category_column = st.selectbox("Filter by", category_columns)
        choices = ["All"] + \
            sorted(data[category_column].dropna().unique().tolist())
        selected_choice = st.selectbox("Choose a value", choices)

        if selected_choice == "All":
            filtered_data = data
        else:
            filtered_data = data[data[category_column] == selected_choice]
    else:
        filtered_data = data

    # Metrics give a quick summary of the filtered data.
    metric_one, metric_two, metric_three = st.columns(3)
    metric_one.metric("Rows", len(filtered_data))
    metric_two.metric("Total", f"{filtered_data[number_column].sum():,.2f}")
    metric_three.metric(
        "Average", f"{filtered_data[number_column].mean():,.2f}")

    st.subheader("Chart")
    st.bar_chart(filtered_data[number_column]) # type: ignore
