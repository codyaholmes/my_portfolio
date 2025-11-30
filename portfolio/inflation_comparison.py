import streamlit as st
import requests
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


st.title("Inflation Comparison")

header = st.container()
with header:
    with st.expander("Summary"):
        st.markdown(
            f"""
            Having a degree in political science, it's hard for me to leave my first love behind sometimes. Over the past election cycles, we've heard a lot about inflation, especially as it relates to recent presidencies. I wanted to compare the data for myself. No news fluff. No political agenda. Just data.
                    
            This data maintains a direct connection with the Federal Reserve's FRED API website. It will update up as new inflation data is posted. Now that's what I call automated reporting!
        """
        )


# Fetch FRED API data
@st.cache_data
def fetch_observations(series_id, start, end):
    api_key = st.secrets.api_keys.fred

    url = (
        "https://api.stlouisfed.org/fred/series/observations?"
        f"series_id={series_id}"
        f"&api_key={api_key}"
        f"&file_type=json"
        f"&observation_start={start}"
        f"&observation_end={end}"
    )

    response = requests.get(url)
    return response.json()["observations"]


# Get presidential terms' data
dt1_data = fetch_observations("CPIAUCSL", "2017-01-01", "2020-12-01")
jb1_data = fetch_observations("CPIAUCSL", "2021-01-01", "2024-12-01")
dt2_data = fetch_observations("CPIAUCSL", "2025-01-01", "2028-12-01")


# Output cleaned dataframes
def cleaned_df(data, pres_term_label):
    df = pd.DataFrame(data)
    df.drop(["realtime_start", "realtime_end", "date"], axis=1, inplace=True)
    df = df.astype({"value": "float64"})

    # Index the CPI to the president's start (YYYY-01-01)
    starting_cpi = df.loc[0, "value"]
    df["value"] = round(df["value"] / starting_cpi * 100, 2)
    df = df.rename(columns={"value": "CPI"})

    # Shift index 1 to make a Month (of presidency) column and add category for presidential terms
    df["Month"] = [i + 1 for i in df.index]
    df["Category"] = pres_term_label
    return df


dt1_df = cleaned_df(dt1_data, "Trump 45")
jb1_df = cleaned_df(jb1_data, "Biden 46")
dt2_df = cleaned_df(dt2_data, "Trump 47")

# Main dataset
cpi_df = pd.concat([dt1_df, jb1_df, dt2_df], axis=0)

st.subheader("Biden vs. Trump Inflation (CPI) Comparison")
st.caption(
    "**Notes**: CPI Growth Index is an easy way to calculate percentage change when starting index at 100. A value of 115 means inflation has grown by 15% (115 - 100 = 15). Month of Presidency is the nth month of a term. Since presidents can only serve four-year terms, 48 is the max."
)


pres_term_options = list(cpi_df["Category"].unique())
# pres_term_options = ["Trump 45", "Biden 46", "Trump 47"]
term_selections = st.multiselect(
    "Select a presidential term",
    pres_term_options,
    default=pres_term_options,
    width="stretch",
)


tabs = ["Chart", "Dataframe"]
main_chart, dataframe = st.tabs(tabs)

with main_chart:
    focused_df = cpi_df.query(f"Category in {term_selections}")
    x = focused_df["Month"]
    y1 = focused_df[focused_df.Category == "Trump 45"]["CPI"]
    y2 = focused_df[focused_df.Category == "Biden 46"]["CPI"]
    y3 = focused_df[focused_df.Category == "Trump 47"]["CPI"]

    fig = go.Figure()
    line_width = 3
    fig.add_trace(
        go.Scatter(
            x=x,
            y=y1,
            name="Trump 45",
            line=dict(color="rgba(167, 0, 22, 0.8)", width=line_width, dash="dot"),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=x,
            y=y2,
            name="Biden 46",
            line=dict(color="#60a5de", width=line_width),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=x,
            y=y3,
            name="Trump 47",
            line=dict(color="#A70016", width=line_width, dash="solid"),
            mode="lines",
        )
    )
    fig.update_layout(
        title=dict(text="CPI Inflation Growth by President (2017-2028)"),
        xaxis=dict(showline=True, linewidth=1.5, mirror=False),
        yaxis=dict(showline=True, linewidth=1.5, mirror=False),
        xaxis_title="Month of Presidency",
        # yaxis_title="CPI Index Growth",
        margin=dict(t=80, l=40, r=40, b=40),
        legend=dict(x=0.01, y=0.99, xanchor="left", yanchor="top"),
    )
    # A cool way to highlight shaded areas within the plot area
    # fig.add_vrect(x0=10, x1=20, fillcolor="#cccccc", opacity=0.2, line_width=1)
    # fig.add_shape(
    #     type="line",
    #     x0=37,
    #     x1=37,
    #     y0=0,
    #     y1=1,
    #     xref="x",
    #     yref="paper",
    #     line=dict(color="#cccccc", width=1.5),
    # )
    # fig.add_annotation(
    #     x=38,
    #     y=1.08,
    #     xref="x",
    #     yref="paper",
    #     text="COVID enters US (Trump 45 term)",
    #     showarrow=False,
    # )
    st.plotly_chart(fig)


with dataframe:
    # Pivot the dataframe so that pres terms get their own columns
    focused_df_pvt = focused_df.pivot(columns="Category", index="Month", values="CPI")
    st.dataframe(focused_df_pvt[term_selections])

st.subheader("Key Takeaways")
st.caption("Takeaways last updated as of November 29, 2025.")
st.markdown(
    """
    - COVID-19 entered the U.S. around January 2020, the 37th month of Trump's first term (45). Inflation drops quite precipitously during that time.
    - Over Biden's term (46), total inflation growth was about 21%.
    - Trump's second term (47) has been marred by slightly higher rates of inflation but is running parallel about the same pace as his first.
"""
)
