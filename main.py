import streamlit as st
import pandas as pd
st.write("CMPD traffic stops")
st.write('Lizeth was here')
@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df
traffic = pd.read_csv('data/Officer_Traffic_Stops.csv')
st.dataframe(traffic)


stops = pd.read_csv('data/Officer_Traffic_Stops.csv')
age_bar=alt.Chart(stops).mark_bar().encode(
    alt.X("Driver_Age", bin=alt.Bin(maxbins=10), title='Driver Age'), 
    y="count():Q", 
    tooltip=['Driver_Age:Q', 'count:Q']
).properties(
    title='Histogram of Driver Age'
)
st.altair_chart(age_bar)
