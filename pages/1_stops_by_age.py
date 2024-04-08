import streamlit as st
import pandas as pd
st.write("CMPD traffic stops")
@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df
stops = pd.read_csv('data/Officer_Traffic_Stops.csv')
st.dataframe(stops)
import altair as alt
## Histogram
age_bar = alt.Chart(stops).mark_bar().encode(
    alt.X("Driver_Age",bin=alt.Bin(maxbins=10)),
    y='count()',
).properties(width=800,height=400)

st.altair_chart(age_bar)