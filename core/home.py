import streamlit as st
from core.data.experience import data as exp_data
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta as rd


st.title("Welcome!")

col1, col2 = st.columns([1, 3])
with col1:
    st.image("core\images\profile_pic.jfif", width=168)
with col2:
    users_name = st.session_state["users_name"]
    users_name = users_name if not None or users_name not in ["", " "] else None
    intro_md = f"""
    Hi{f", :yellow-background[{users_name}]!" if users_name else "!"}👋 My name is Cody Holmes. Thanks for checking out my online portfolio. It's made with Python's `streamlit` library, which I really dig.

    I'm a BI developer, and I love all things data. When I'm not riding my [OneWheel](https://google.com), I'm learning something new. Recently, I've been dabbling with Django and React, just 'cause. Since, I'm a data nerd, I guess it makes sense to display some data—about me. Allow me to dashboard-ize myself here.
    """
    st.markdown(intro_md)

st.space("small")

col1, col2, col3 = st.columns(3)
with col1:
    starts = [dt.strptime(i["start"], "%Y-%m-%d") for i in exp_data]
    ends = [
        dt.strptime(i["end"], "%Y-%m-%d") if i["end"] else dt.now() for i in exp_data
    ]
    total_exp_yrs = 0
    for start, end in zip(starts, ends):
        datedelta = rd(end, start)
        total_exp_yrs += datedelta.years
        total_exp_yrs += datedelta.months / 12

    st.metric(
        "Total Experience",
        f"{total_exp_yrs} years",
        border=True,
        help="This calculation comes from the dates listed in the Experience section of my Resume page.",
    )
with col2:
    st.metric(
        "Freelance Hours",
        f"352 hours",
        border=True,
        help="Total of my Upwork and personal client hours.",
    )
with col3:
    st.metric("Upwork Rating", "100%", border=True)

st.subheader("Navigating this Portfolio")
st.markdown(
    """
    To the left should be a sidebar, which will allow you to see my interactive resume, or you can view a portfolio of pet projects I've done in my free time. After all, that is the purpose of this app, to highlight my skillz.
            
    On the portfolio projects, you will find a summary. I've included some skill badges at the bottom of the pages to also categorize the skills I applied for that project. (If you need some context on the skill badges, check out my resume, specifically the "Skills" section.)
"""
)
