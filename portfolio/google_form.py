import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import date, datetime, timezone
import time
import uuid

worksheet_viewer_url = "https://docs.google.com/spreadsheets/d/1d3UxAwOAz-rYsZjn_f4Qic-msmPzOwLf4127hAxBOyc/edit?usp=sharing"

st.title("Google Sheets Intake")
with st.expander("Summary"):
    st.markdown(
        f"""
        Great data visualization starts with great data entry. And while Google Sheets doesn't really serve as a great database, it does the job here.

        This page is just a highlight of my skills to navigate an API and send data in a modeled way. The form below has a many-to-one relationship among certain fields. You can see how I land that data into two "tables" in [this]({worksheet_viewer_url}) Google Sheet.
    """
    )

# Google Sheets auth and connection
cred_keys = {
    "type": st.secrets.google.type,
    "project_id": st.secrets.google.project_id,
    "private_key_id": st.secrets.google.private_key_id,
    "private_key": st.secrets.google.private_key,
    "client_email": st.secrets.google.client_email,
    "client_id": st.secrets.google.client_id,
    "auth_uri": st.secrets.google.auth_uri,
    "token_uri": st.secrets.google.token_uri,
    "auth_provider_x509_cert_url": st.secrets.google.auth_provider_x509_cert_url,
    "client_x509_cert_url": st.secrets.google.client_x509_cert_url,
    "universe_domain": st.secrets.google.universe_domain,
}
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_info(cred_keys, scopes=scopes)
client = gspread.authorize(creds)
sheet_id = "1d3UxAwOAz-rYsZjn_f4Qic-msmPzOwLf4127hAxBOyc"
form_worksheet = client.open_by_key(sheet_id).worksheet("Form Data")
avengers_worksheet = client.open_by_key(sheet_id).worksheet("Avenger Selections")

st.subheader("Fake Name Verification")
st.caption(
    """
    We've all signed up for a service where we don't want to put in our _real_ information. With that in mind, give me your best fake names you use with some random data collection below. For _The Office_ fans out there, this is like Michael Scott's "Orville Tootenbacher" moniker!
"""
)

tabs = ["Form", "Responses"]
form, responses = st.tabs(tabs)
with form:
    with st.form("fake_name_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            st.text_input(
                "Name (Required)", key="fake_name", placeholder="Please keep it PC..."
            )
        with col2:
            st.date_input(
                "Fake Birthday",
                value="today",
                min_value=date(1920, 1, 1),
                max_value="today",
                key="fake_bday",
                format="MM/DD/YYYY",
            )

        col1, col2 = st.columns(2)
        with col1:
            st.text_input(
                "Fake Password",
                help="For all that is holy, DO NOT PUT A REAL PASSWORD IN HERE!",
                type="password",
                key="fake_pw",
            )
        with col2:
            st.markdown(
                """<p style="font-size: 14px">Pineapple on pizza?</p>""",
                unsafe_allow_html=True,
            )
            st.checkbox("I agree", key="pineapple_on_pizza")

        st.slider(
            "How goofy is your fake name on a scale 1-10?",
            min_value=1,
            max_value=10,
            key="goofy_rating",
        )

        avenger_options = [
            "🐜 Ant-Man",
            "🐈‍⬛ Black Panther",
            "🕸️ Black Widow",
            "🛡️ Captain America",
            "🎯 Hawkeye",
            "💪 Hulk",
            "🪫 Iron Man",
            "🔨 Thor",
            "🤔 Other",
        ]
        st.multiselect(
            "Best Avengers? (Select more than one.)",
            avenger_options,
            key="best_avenger",
        )

        st.text_area("Penny for your thoughts?", key="penny_thoughts")

        submitted = st.form_submit_button("Submit")

# Post-form logic
if submitted:
    unique_id = str(uuid.uuid4())
    utc_now = datetime.now(timezone.utc).strftime("%m/%d/%Y %H:%M:%S")

    errors = []
    name = st.session_state.fake_name

    if not name:
        errors.append("Provide a name")

    if errors:
        for err in errors:
            st.error(err)

    else:
        form_data = [
            unique_id,
            utc_now,
            st.session_state["fake_name"],
            st.session_state["fake_bday"].strftime("%m/%d/%Y"),
            st.session_state["fake_pw"],
            st.session_state["pineapple_on_pizza"],
            st.session_state["goofy_rating"],
            st.session_state["penny_thoughts"],
        ]
        # Cleans avenger text and sends to second sheet due to many-to-one relationship
        avengers_data = [
            [unique_id, utc_now, avenger.split(" ", maxsplit=1)[1]]
            for avenger in st.session_state.best_avenger
        ]
        with st.spinner("Sending your data through the interwebz...", show_time=True):
            form_worksheet.append_row(form_data)
            avengers_worksheet.append_rows(avengers_data)
            time.sleep(2)
        st.success(
            f"Form submitted successfully! See where your submission went [here]({worksheet_viewer_url})"
        )


with responses:
    st.write("Under construction...")
