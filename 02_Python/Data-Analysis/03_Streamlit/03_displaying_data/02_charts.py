"""
Topic: Charts — st.line_chart(), st.bar_chart(), st.area_chart(), 
and embedding a Plotly/Matplotlib chart with st.plotly_chart() / st.pyplot()

Notes:
- A line chart is useful for showing change over time.
- A bar chart compares values between categories.
- An area chart is like a line chart with the space below it filled in.
- Plotly and Matplotlib let you create more custom charts.
- Run this file with: streamlit run 02_charts.py
"""

import streamlit as st
import pandas as pd


st.title("Simple Charts")
st.write("These charts use a small table of weekly sales.")

# Each row is one week. Each column contains sales for one product.
data = pd.DataFrame(
    {
        "Week": ["Week 1", "Week 2", "Week 3", "Week 4"],
        "Apples": [10, 14, 12, 18],
        "Bananas": [8, 11, 15, 13],
    }
).set_index("Week")

st.subheader("Our data")
st.dataframe(data)  # type: ignore

# Line charts show how values change.
st.subheader("Line chart")
st.line_chart(data)  # type: ignore

# Bar charts make category comparisons easy.
st.subheader("Bar chart")
st.bar_chart(data)  # type: ignore

# Area charts highlight the size of values over time.
st.subheader("Area chart")
st.area_chart(data)  # type: ignore

# Plotly is useful when you need an interactive chart.
# Uncomment these lines after installing Plotly with: pip install plotly
# import plotly.express as px
# figure = px.line(data, x=data.index, y=["Apples", "Bananas"], markers=True)
# st.plotly_chart(figure, use_container_width=True)

# Matplotlib is useful when you want detailed control over a chart.
# Uncomment these lines after installing Matplotlib with: pip install matplotlib
# import matplotlib.pyplot as plt
# figure, axis = plt.subplots()
# axis.plot(data.index, data["Apples"], marker="o", label="Apples")
# axis.set_title("Apple sales")
# axis.set_xlabel("Week")
# axis.set_ylabel("Sales")
# axis.tick_params(axis="x", labelrotation=45)  # Adjust the x-axis label angle.
# axis.legend()
# st.pyplot(figure)
