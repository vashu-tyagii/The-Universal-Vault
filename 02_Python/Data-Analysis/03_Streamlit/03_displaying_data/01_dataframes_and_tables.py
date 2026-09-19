"""
Topic: Displaying data — st.dataframe(), st.table(), st.metric()

Notes:
- st.dataframe() shows an interactive table. Users can sort and explore it.
- st.table() shows a simple, static table.
- st.metric() highlights one important number.
"""

import pandas as pd
import streamlit as st


st.title("Displaying Data")

# A small DataFrame is easy to read and use in examples.
sales = pd.DataFrame(
	{
		"Product": ["Notebook", "Pen", "Backpack"],
		"Units sold": [25, 80, 12],
		"Price": [5.00, 1.50, 30.00],
	}
)

# Interactive table: useful when users need to explore the data.
st.subheader("Interactive DataFrame")
st.dataframe(sales, use_container_width=True)  # type: ignore

# Static table: useful for displaying a small, fixed table.
st.subheader("Simple Table")
st.table(sales) # type: ignore

# Metric: useful for showing one important value.
total_units = int(sales["Units sold"].sum())
st.subheader("Key Metric")
st.metric(label="Total units sold", value=total_units)
