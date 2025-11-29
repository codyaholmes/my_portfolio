import streamlit as st
import streamlit.components.v1 as components

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

st.title("HR Analytics")
st.subheader("Summary")
st.text(
    "Lorem ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis officiis minima ullam nobis omnis laborum reprehenderit quas! Quia quos, mollitia fugit obcaecati, consectetur deserunt, incidunt animi illum itaque optio aperiam libero iste ipsum repudiandae pariatur aliquid ipsam dolorem illo quas!"
)

st.caption(
    "**Note**: If you are viewing on mobile, the iframe may not work as expected! Desktop view is recommended."
)
components.iframe(
    "https://app.powerbi.com/view?r=eyJrIjoiY2Q5YjlmMTctZGU0Zi00NzE1LTkzNGUtOTlmYjVjNjJhZDU0IiwidCI6IjcwZGUxOTkyLTA3YzYtNDgwZi1hMzE4LWExYWZjYmEwMzk4MyIsImMiOjN9",
    height=800,
    width=width,
)
