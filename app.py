import streamlit as st

home = st.Page("core/home.py", title="Welcome", icon=":material/home:", default=True)
resume = st.Page("core/resume.py", title="Resume", icon=":material/work:")
inflation_comparison = st.Page(
    "portfolio/inflation_comparison.py",
    title="Inflation Comparison",
    icon=":material/money_bag:",
)
hr_analytics = st.Page(
    "portfolio/hr_analytics.py", title="HR Analytics", icon=":material/people:"
)
platos_pizza = st.Page(
    "portfolio/platos_pizza.py", title="Plato's Pizza", icon=":material/local_pizza:"
)
book_scraper = st.Page(
    "portfolio/book_scraper.py", title="Book Scraper", icon=":material/book:"
)
google_form = st.Page(
    "portfolio/google_form.py",
    title="Google Sheets Intake",
    icon=":material/add_row_above:",
)
# search = st.Page("tools/search.py", title="Search", icon=":material/search:")
# history = st.Page("tools/history.py", title="History", icon=":material/history:")
pages = {
    "General": [home, resume],
    "Portfolio": [
        inflation_comparison,
        hr_analytics,
        platos_pizza,
        book_scraper,
        google_form,
    ],
    # "Tools": [search, history],
}

pg = st.navigation(pages=pages)
with st.sidebar:
    st.text_input(
        "What is your name?",
        key="users_name",
        help="Names are special. I'd like to address you personally in my app. No data collection here!",
    )

pg.run()
