

import streamlit as st
import time
from datetime import datetime


st.title("child TB deaths;live estimated counter")
st.write("this is a live counter of child TB DEATHS:,one death every 3 minutes")
SECONDS_PER_DEATH=3*60


placeholder =st.empty()

while True:
    now = datetime.now()
    start_of_year = datetime(now.year, 1, 1)
    start_of_day = datetime(now.year, now.month, now.day)

    seconds_since_start_of_year = (now - start_of_year).total_seconds()
    seconds_since_start_of_day = (now - start_of_day).total_seconds()
    deaths_since_start_of_year = int(seconds_since_start_of_year / SECONDS_PER_DEATH)
    deaths_since_start_of_day = int(seconds_since_start_of_day / SECONDS_PER_DEATH)
    seconds_until_next_death = SECONDS_PER_DEATH - (seconds_since_start_of_day % SECONDS_PER_DEATH)


    with placeholder.container():
        st.metric(
            f"death since start of year:{deaths_since_start_of_year}",
            f"deaths since start of day: {deaths_since_start_of_day}",
            f"seconds until next death: {seconds_until_next_death}",
        )
        st.caption("source:WHO Global TB Report.Estimate for educational purposes only")

    time.sleep(1)






