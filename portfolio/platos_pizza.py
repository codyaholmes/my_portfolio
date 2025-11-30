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

st.title("Plato's Pizza")

with st.expander("Summary"):
    st.markdown(
        """
        Creatively designed dashboard made with Power BI. This product was a result of a [data challenge](https://mavenanalytics.io/challenges/maven-pizza-challenge) offered by Maven Analytics. This project exemplifies my ability to build highly customized and stylized reports that draw user attention. For example, my favorite visualization is the weekly-time heatmap, showing stakeholders where the busiest times are.
        """
    )

st.caption(
    "**Note**: If you are viewing on mobile, the iframe may not work as expected! Desktop view is recommended."
)
components.iframe(
    "https://app.powerbi.com/view?r=eyJrIjoiOWYzYjA3ODQtMjhkMi00NGRjLTg1NzEtM2YxYWUyNzk2ZDNjIiwidCI6IjcwZGUxOTkyLTA3YzYtNDgwZi1hMzE4LWExYWZjYmEwMzk4MyIsImMiOjN9",
    height=1510,
    width=width,
)
