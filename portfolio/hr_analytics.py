import streamlit as st
import streamlit.components.v1 as components


st.title("HR Analytics")

# PAGE STYLING
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

# SUMMARY SECTION
with st.expander("Summary"):
    st.markdown(
        """
        Using a sample human resources [dataset](https://www.kaggle.com/datasets/rhuebner/human-resources-data-set) from Kaggle, this data was cleaned to derve a simple, executive-ready sample of common HR metrics, such as headcount and turnover. One cool hidden feature of this report is its hover features. I like to give my end-users as much context as possible without taking up real estate. Try hovering over every colored card in the dashboard to gain some important context! Another important design element that I included was the coordination of colors. Headcount is :blue-background[blue]. Terminations are :orange-background[orange]. Turnover is :violet-background[violet], etc. This strategy makes the audience implicity associate ideas across the page.
    """
    )

# DASHBOARD AREA
dashboard = st.container()
with dashboard:
    st.caption(
        "**Note**: If you are viewing on mobile, the iframe may not work as expected! Desktop view is recommended."
    )
    components.iframe(
        "https://app.powerbi.com/view?r=eyJrIjoiY2Q5YjlmMTctZGU0Zi00NzE1LTkzNGUtOTlmYjVjNjJhZDU0IiwidCI6IjcwZGUxOTkyLTA3YzYtNDgwZi1hMzE4LWExYWZjYmEwMzk4MyIsImMiOjN9",
        height=800,
        width=width,
    )
