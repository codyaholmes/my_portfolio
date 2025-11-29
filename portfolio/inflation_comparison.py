import streamlit as st

st.title("Inflation Comparison")
st.subheader("Summary")
st.text("Lorem ipsum " * 20)
width = 1400
st.html(
    f"""
    <style>
        .stMainBlockContainer {{
            max-width: {width}px;
        }}
    </style>
"""
)
