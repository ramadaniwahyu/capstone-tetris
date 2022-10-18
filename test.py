import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

from vega_datasets import data

source = data.cars()

c = alt.Chart(source).transform_calculate(
    url='https://www.google.com/search?q=' + alt.datum.Name
).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    colorvalue='red'
    href='url:N',
    tooltip=['Name:N', 'url:N']
)

# st.table(source)

st.altair_chart(c, use_container_width=True)