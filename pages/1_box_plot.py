stops = pd.read_csv('data/Officer_Traffic_Stops.csv')
age_bar=alt.Chart(stops).mark_bar().encode(
    alt.X("Driver_Age", bin=alt.Bin(maxbins=10), title='Driver Age'), 
    y="count():Q", 
    tooltip=['Driver_Age:Q', 'count:Q']
).properties(
    title='Histogram of Driver Age'
)
st.altair_chart(age_bar)