"""
Topic: Layout — st.sidebar, st.columns(), st.container(), st.tabs()

Run this file with:
	streamlit run 02_layout_columns_sidebar.py

Simple layout notes:
	- st.sidebar puts controls in a sidebar.
	- st.columns() places content next to each other.
	- st.container() groups content together.
	- st.tabs() separates content into tabs.
"""

import streamlit as st


st.title("Simple Streamlit Layout")
st.write("This page shows a sidebar, columns, a container, and tabs.")

# Sidebar: useful for settings and user inputs.
with st.sidebar:
    st.header("Settings")
    name = st.text_input("Your name", "Friend")
    show_message = st.checkbox("Show a message", value=True)

if show_message:
    st.success(f"Hello, {name}!")

# Columns: display content side by side.
left_column, right_column = st.columns(2)

with left_column:
    st.subheader("Left column")
    st.write("This content is on the left.")

with right_column:
    st.subheader("Right column")
    st.write("This content is on the right.")

# Container: keep related content in one layout block.
with st.container(border=True):
    st.subheader("A container")
    st.write("A container groups related content together.")
    st.info("Containers are useful when a section needs a clear boundary.")

# Tabs: show different content without making the page too long.
first_tab, second_tab = st.tabs(["About", "Tips"])

with first_tab:
    st.write("Use layouts to make an app easier to read.")

with second_tab:
    st.write("Put simple controls in the sidebar and related content in containers.")
