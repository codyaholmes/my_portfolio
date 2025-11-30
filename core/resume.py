import streamlit as st
from core.data.skills import data as skills_data
from core.data.experience import data as experience_data
from core.data.certifications import data as certs_data
from core.data.education import data as edu_data
from datetime import datetime
import json
import time


st.title("Cody Holmes, MPA")


@st.dialog("Contact Info")
def show_info():
    st.markdown(
        ":gray-badge[:material/email:] [codyaholmes@outlook](mailto:codyaholmes@outlook.com)"
    )
    st.markdown(":gray-badge[:material/mobile_2:] (915) 929-3006")
    st.markdown(":gray-badge[:material/map:] Denton, Texas")
    st.markdown(
        ":gray-badge[:material/workspaces:] [LinkedIn](https://www.linkedin.com/in/cody-a-holmes/)"
    )
    st.markdown(
        ":gray-badge[:material/email:] [Upwork](https://www.upwork.com/freelancers/~018b6a05db669d68fe)"
    )


if "show_info" not in st.session_state:
    if st.button("See contact info"):
        show_info()

text = "Analytics leader with 10+ years of experience turning data into business strategy. Proven track record in leading cross-functional teams, scaling reporting systems, leading data warehousing, and driving organizational transformation through analytics. Skilled at translating data into action—and action into results!."
st.caption(text)

# Order of tabs matters in how they are displayed
tabs = ["Experience", "Education", "Certifications", "Skills"]
experience, education, certifications, skills = st.tabs(tabs)

with experience:
    expanding = st.toggle("Expand/Collapse", value=False, key="exp_expand")
    show_bullets = False
    # show_bullets = st.toggle("Summary/Bullets", value=False)

    for exp in experience_data:
        position = exp["position"]
        employer = exp["employer"]
        location = exp["location"]
        remote = exp["remote"]
        start = datetime.strptime(exp["start"], "%Y-%m-%d").strftime("%B %Y")
        end = (
            datetime.strptime(exp["end"], "%Y-%m-%d").strftime("%B %Y")
            if exp["end"]
            else "Present"
        )
        summary = exp["summary"]
        bullets = exp["bullets"]

        with st.expander(position, expanded=expanding):
            st.markdown(f"##### {employer}")

            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f":material/calendar_today: **{start} -> {end}**")
            with col2:
                if remote:
                    st.markdown(
                        f'<div style="text-align: right;"><b>{location}</b> ☑️ Remote</div>',
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(
                        f'<div style="text-align: right;"><b>{location}</b></div>',
                        unsafe_allow_html=True,
                    )

            if summary and not show_bullets:
                st.text(summary)
            if bullets and show_bullets:
                bullet_list_markdown = [f"- {b}" for b in bullets]
                bullets_markdown = "\n".join(bullet_list_markdown)
                st.markdown(bullets_markdown)

    st.space("small")
    st.markdown(
        "I love **data democratization**. 😎 Feel free to download my experience data and play with it!"
    )
    experience_json = json.dumps(experience_data)

    with st.expander("JSON Preview", expanded=False):
        st.json(experience_json, expanded=True)
    with st.expander("CSV Preview"):
        st.dataframe(experience_data)

    # Data download options
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.download_button(
            "JSON",
            data=experience_json,
            file_name="cody_holmes_experience.json",
            mime="application/json",
            icon=":material/download:",
            width="stretch",
        )
    with col2:
        st.download_button(
            "CSV",
            data="data here...",
            file_name="cody_holmes_experience.csv",
            mime="text/csv",
            icon=":material/download:",
            width="stretch",
        )
    with col3:
        st.download_button(
            "Excel",
            data="data here...",
            file_name="cody_holmes_experience.xls",
            mime="application/vnd.ms-excel",
            icon=":material/download:",
            width="stretch",
        )
    with col4:
        with open("core\data\Cody Holmes Resume.pdf", "rb") as f:
            pdf = f.read()
        st.download_button(
            "PDF",
            data=pdf,
            file_name="Cody Holmes Resume.pdf",
            mime="application/pdf",
            icon=":material/download:",
            width="stretch",
        )

with education:
    expanding = st.toggle("Expand/Collapse", value=True, key="edu_expand")

    for edu in edu_data:
        degree = edu["degree"]
        school = edu["school"]
        start = edu["start"]
        end = edu["end"]
        location = edu["location"]
        bullets = edu["bullets"]

        with st.expander(degree, expanded=expanding):
            st.markdown(f"##### {school}")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f":material/calendar_today: **{start} -> {end}**")
            with col2:
                st.markdown(
                    f'<div style="text-align: right;"><b>{location}</b></div>',
                    unsafe_allow_html=True,
                )
            if bullets:
                bullet_list_markdown = [f"- {b}" for b in bullets]
                bullets_markdown = "\n".join(bullet_list_markdown)
                st.markdown(bullets_markdown)

with certifications:
    expanding = st.toggle("Expand/Collapse", value=True, key="cert_expand")

    for cert in certs_data:
        name = cert["name"]
        agency = cert["agency"]
        link = cert["link"]
        issued = (
            datetime.strptime(cert["issued"], "%Y-%m-%d")
            .strftime("%B %d, %Y")
            .replace(" 0", "")
        )
        expiration = (
            datetime.strptime(cert["expiration"], "%Y-%m-%d")
            .strftime("%B %d, %Y")
            .replace(" 0", "")
        )
        number = cert["number"]

        with st.expander(name, expanded=expanding):
            st.markdown(f"##### {agency}")
            st.markdown(f":material/calendar_today: {start} -> {end}")
            if number:
                st.markdown(f"- Certication Number: {number}")
            if link:
                st.link_button("See certification", url=link)

with skills:
    st.markdown("**Skills Legend**")
    st.markdown(
        """
        :gray-badge[Beginner] -> :violet-badge[Intermediate] -> :blue-badge[Advanced] -> :green-badge[Expert]
        - - -
    """
    )

    markdown_list = []
    # Sort skills; if no name found use triple z to put it at the end
    skills_data = sorted(skills_data, key=lambda item: item.get("name", "zzz"))

    for skill in skills_data:
        name = skill.get("name", "Skill")
        icon = skill.get("icon", "")
        level = skill.get("level", "intermediate")

        if level == "beginner":
            color = "gray"
        elif level == "intermediate":
            color = "violet"
        elif level == "advanced":
            color = "blue"
        elif level == "expert":
            color = "green"
        else:
            pass

        markdown_list.append(f":{color}-badge[:material/{icon}: {name}]")

    st.markdown(" ".join(markdown_list))
