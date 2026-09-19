# Streamlit — Quick Reference Notes

Short "what it does" + minimal syntax. Use this for revision.

---

## Basic App Structure

### Title, Headers, Text

```python
st.title("My App")
st.header("Section Header")
st.subheader("Sub Section")
st.write("Any text, number, or DataFrame")
st.text("Plain text")
```

### Running the app

```bash
streamlit run app.py
```

---

## Layout

**Sidebar** — puts content in a collapsible side panel

```python
st.sidebar.selectbox("Choose", ["A", "B"])
```

**Columns** — side-by-side layout

col1, col2 = st.columns(2)
col1.write("Left")
col2.write("Right")

with st.container():
    st.write("Grouped content")

```


**Tabs** — multiple views in one page
```python
tab1, tab2 = st.tabs(["Overview", "Details"])
with tab1:
    st.write("Overview content")
```

---

## Input Widgets

```python
st.text_input("Enter name")
st.number_input("Enter age")
st.selectbox("Choose option", ["A", "B", "C"])
st.slider("Pick a value", 0, 100)
st.checkbox("Agree?")
st.radio("Choose one", ["Yes", "No"])
st.button("Click me")
```

---

## Session State

**Keep values persistent across reruns** (Streamlit reruns the whole script
on every interaction — session_state prevents values from resetting)

```python
if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment"):
    st.session_state.counter += 1

st.write(st.session_state.counter)
```

---

## Displaying Data

**DataFrame / Table**

```python
st.dataframe(df)      # interactive, scrollable
st.table(df)           # static table
```

**Metric** — highlight a single KPI number

```python
st.metric(label="Total Sales", value="₹5.2L", delta="+12%")
```

---

## Charts

**Built-in charts (quick, simple)**

```python
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)
```

**Plotly / Matplotlib (more control/customization)**

```python
st.plotly_chart(fig)
st.pyplot(fig)
```

---

## File Upload

**Let user upload a file, read it into Pandas**

uploaded_file = st.file_uploader("Choose a CSV file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

```

---

## Filtering with a Widget (Common Dashboard Pattern)

```python
course = st.selectbox("Select Course", df["Course"].unique())
filtered_df = df[df["Course"] == course]
st.dataframe(filtered_df)
```

---

## Common Gotchas (Worth Remembering)

- Streamlit **reruns the entire script top-to-bottom** every time you
  interact with a widget — this is why session_state exists, to preserve
  values across those reruns.
- `st.dataframe()` is interactive (sortable, scrollable); `st.table()` is
  static — use `st.dataframe()` for most dashboard use cases.
- Widgets need a unique `key=` parameter if you use the same widget type
  more than once on a page, otherwise Streamlit may throw a duplicate
  element error.
