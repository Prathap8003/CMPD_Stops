import streamlit as st
import pandas as pd
st.write("CMPD traffic stops")
@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df
traffic = pd.read_csv('data/Officer_Traffic_Stops.csv')
st.dataframe(traffic)



