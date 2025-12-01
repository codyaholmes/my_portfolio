import streamlit as st
from core.data.experience import data as exp_data
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta as rd
from pathlib import Path
import streamlit.components.v1 as components
import requests
import random


st.title("Welcome!")

# HEADER SECTION
col1, col2 = st.columns([1, 3])
with col1:
    st.image(str(Path("core") / "images" / "profile_pic.jfif"), width=168)
with col2:
    users_name = st.session_state["users_name"]
    users_name = users_name if not None or users_name not in ["", " "] else None
    intro_md = f"""
    Hi{f", :yellow-background[{users_name}]!" if users_name else "!"}👋 My name is Cody Holmes. Thanks for checking out my online portfolio. It's made with Python's [streamlit](https://streamlit.io/) library, which I really dig.

    I'm a BI developer, and I love all things data. When I'm not riding my OneWheel (see below), I'm learning something new. It's important that I apply my new skills, and that's one of the purposes of this portfolio. Hope you enjoy it. My contact info is on my Resume page.
    """
    st.markdown(intro_md)

with st.expander("Summary"):
    st.markdown(
        f"""
    Just about every page will have one of these summary expanders, which provides some brief context for a project or just helps shrink some of the page material. For the most part, they are collapsed by default. But I've put one here so that you can expect them and get used to expanding them.
    """
    )

# METRICS SECTION #
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
        total_exp_yrs += round(datedelta.months / 12, 2)

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
    st.metric(
        "Upwork Rating",
        "100%",
        border=True,
        help="I also have Upwork's **Top Talent** badge!",
    )

st.caption("As a BI developer, it only makes sense that I metric-ize myself...")

# NAVIGATION SECTION
st.subheader("Navigating this Portfolio")
st.markdown(
    f"""
    To the left should be a sidebar. If you're on mobile,{f" :yellow-background[{users_name}]," if users_name else ""} there should be a double chevron in the top-right that will expand it. There, you will find different pet projects I've made to showcase different skills. There is also a link to view my resume under the "General" section. If you don't like the interactive version, you can download a PDF copy. I've also included the ability to download my resume data in a structured format. Take it. Put in an AI model, and ask it to summarize me as a candidate!
"""
)

# PERSONAL SECTION
st.subheader("More Personal")
st.markdown(
    "Being a dad of two boys, I'm no stranger to two things: wrestling and telling a 🌽⚽ dad joke. Might as well start there, right?"
)


# Get dad joke
def get_dad_jokes(keyword=None):
    url_base = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}

    if keyword == "" or keyword is None:
        response = requests.get(url_base, headers=headers)
        return "> " + response.json()["joke"].replace("\r\n", " ")

    if keyword:
        response = requests.get(f"{url_base}search?term={keyword}", headers=headers)
        results = response.json()["results"]
        jokes = [i["joke"] for i in results]

        if jokes:
            return "> " + random.choice(jokes).replace("\r\n", " ")
        else:
            return f"> No dad jokes found with the term: **{keyword}**"


with st.container(border=True):
    col1, col2 = st.columns(2, vertical_alignment="bottom")
    with col1:
        keyword = st.text_input("Dad joke topic", placeholder="Ex: dog")
    with col2:
        st.button("Get random", on_click=get_dad_jokes)

    laugh_emojis = ["😀", "😄", "😁", "😆", "😅", "🤣", "😂", "😹"]
    emoji = random.choice(laugh_emojis)
    st.markdown(f"{get_dad_jokes(keyword)} {emoji}")

st.markdown(
    """
    Other than telling dad jokes, I'm a huge football fan, but I'll watch other sports from time to time. Some of my favorite teams are listed below.
    - Dallas Cowboys - a miserable existence
    - Texas Longhorns
    - Texas Rangers
    - Dallas Mavericks
"""
)

st.markdown(
    """

"""
)

# ONEWHEEL SECTION
st.markdown("##### A OneWheel? What's that?")
st.caption(
    "Only the coolest thing ever. Data trolls need to get their Vitamin D somehow..."
)
components.iframe(
    "https://www.youtube.com/embed/XNqOU4jx62I?si=3WkukAbwRWxseX5B", height=400
)
