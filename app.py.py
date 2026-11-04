
import streamlit as st

st.title("firstprogram tb")

minutes = 3
per_hour=60 // minutes
per_day=per_hour*24
per_year=per_day*365


st.metric("per hour", per_hour)
st.metric("per day" , per_day)
st.metric("per year", per_year)


st.caption("Source: WHO GLOBAL TB REPORT.For education only")








