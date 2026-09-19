"""Simple notes and example: Streamlit session state.

Streamlit reruns this file whenever a user interacts with the page. Normal
variables are created again on each rerun, but ``st.session_state`` keeps
values for that user's session.
"""

import streamlit as st


# Create the value only once. This prevents it from resetting after a click.
if "count" not in st.session_state:
    st.session_state.count = 0


st.title("Session State: Simple Counter")
st.write("The counter keeps its value when you click the button.")

if st.button("Add 1"):
    st.session_state.count += 1

st.write(f"Count: {st.session_state.count}")

if st.button("Reset"):
    st.session_state.count = 0
    st.rerun()
