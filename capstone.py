import altair as alt
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

header="""<style>
.header {
background-image: url('https://ramadani.my.id/capstone-tetris/header.jpg');
background-size: cover; /* Resize the background image to cover the entire container */
text-align: center;
}
</style>
<div class="header">
<br /><br /><br /><br /><br />
<br /><br /><br /><br /><br />
</div>
"""
st.markdown(header,unsafe_allow_html=True)

st.title('Manusia dan Pandemi Covid-19')

df = pd.read_excel('covid.xlsx')
df2 = pd.read_excel('covid.xlsx', sheet_name='Sheet2')

st.subheader('Jumlah Kasus Covid di Indonesia')
st.altair_chart(
    alt.Chart(df)
    .transform_fold(
        ['Total kasus', 'Sembuh', 'Meninggal Dunia'],
        as_=['Total', 'Data Kasus Covid-19']
    )
    .mark_line(color='red')
    .encode(
        alt.X('date'),
        alt.Y('Data Kasus Covid-19:Q', stack=None),
        alt.Color('Total:N')
    ),
    use_container_width=True
)

st.subheader('Timeline Kasus Covid')
st.altair_chart(
    alt.Chart(df)
    .transform_fold(
        ['% kasus aktif', 'Tingkat kesembuhan (seluruh kasus)', 'Tingkat kematian (seluruh kasus)'],
        as_=['Total', 'Kasus Covid-19']
    )
    .mark_line(color='red')
    .encode(
        alt.X('date'),
        alt.Y('Kasus Covid-19:Q', stack=None),
        alt.Color('Total:N')
    ),
    use_container_width=True
)

st.subheader('Data Lain')
st.altair_chart(
    alt.Chart(df2)
    .transform_fold(
        ['AHH-Lk', 'AHH-Pr', 'IPM'],
        as_=['Total', 'Data Lain']
    )
    .mark_line(color='red')
    .encode(
        alt.X('tahun'),
        alt.Y('Data Lain:Q', stack=None),
        alt.Color('Total:N')
    ),
    use_container_width=True
)

st.subheader('Data Lain2')
st.altair_chart(
    alt.Chart(df2)
    .transform_fold(
        ['PDB', 'Poverty Headcount ratio', 'Population Growth', 'Unemployee rate'],
        as_=['Total', 'Data']
    )
    .mark_line(color='red')
    .encode(
        alt.X('tahun'),
        alt.Y('Data:Q', stack=None),
        alt.Color('Total:N')
    ),
    use_container_width=True
)
# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c'])

# st.line_chart(chart_data)

# st.table(chart_data)