import altair as alt
import streamlit as st
import pandas as pd
import numpy as np
from numerize import numerize

st.set_page_config(layout="wide")

df = pd.read_csv('dataset.csv')

df['Participant'] = df['Participant'].astype(str)
df['Sons'] = df['Sons'].astype(str)

st.title('Manusia dan Pandemi Covid-19')
st.write('Dicky Wahyu Ramadani - TETRIS PROA - Oktober 2022')

st.header('Pendahuluan')
st.write(
    'Pandemi Covid-19 telah membuat banyak orang di dunia ini merasakan tekanan psikologis yang berat mulai dari sulitnya berinteraksi dengan keluarga, teman, tetangga dan banyak orang lainnya, belum lagi apabila harus menjalani masa isolasi yang dapat memberikan tekanan yang sangat berat bagi manusia sebagai mahluk sosial. Lalu bagaimana dampaknya terhadap kita sebagai manusia?'
)

st.header('Data dan Metodologi')
st.subheader('Data')
st.write(
    'Data yang digunakan diambil dari [sini](https://figshare.com/articles/dataset/Covid-19_and_Character_Strengths/12366494). Data ini merupakan hasil survey yang dilaksanakan terhadap participant dengan informasi sebagai berikut:'
    )

met1, met2, met3 = st.columns(3)
with met1:
    st.metric("Total Participants",df['Participant'].nunique())

with met2:
    st.metric("Participants with Kids", df['Sons'].value_counts()['1'])
    
with met3:
    st.metric("Participants with No Kids", df['Sons'].value_counts()['0'])

participant_seg, gender_seg = st.columns(2)
with participant_seg:
    st.subheader('Occupation')
    st.bar_chart(
        df.groupby('Student').nunique()['Participant']
    )
    
with gender_seg:
    st.subheader('Gender')
    st.bar_chart(
        df.groupby('Gender').nunique()['Participant']
    )
    
 
st.subheader('Metodologi')
st.write('Data ini diambil dengan cara penyebaran kuesioner yang berisikan beberapa materi antara lain: Values in Action Inventory of Strengths-120 (VIA-IS-120) yang digunakan untuk mengukur kekuatan karakter (Character Strength); Depression, Anxiety, and Stress Scales-21 (DASS-21) yang digunakan untuk mengukur tingkat stress, depresi dan kecemasan yang dirasakan selama masa pandemi; General Health Questionnaire-12 (GHQ-12) digunakan untuk mengukur kesehatan psikologis secara umum; dan yang terakhir, Self-efficacy measure for Covid-19 (SEC), digunakan untuk mengukur kepercayaan terhadap diri sendiri untuk mengatasi hal-hal dalam kehidupan sehari-hari selama masa pandemi.')
st.markdown('**Values in Action Inventory of Strengths-120**')
st.markdown('**Depression, Anxiety, and Stress Scales-21 (DASS-21)**')
st.markdown('**General Health Questionnaire-12 (GHQ-12)**')
st.markdown('**Self-efficacy measure for Covid-19 (SEC)**')
st.subheader('Data Survey')
st.dataframe(df)

st.subheader('Component Analysis')
ds = pd.DataFrame(df.describe(include=[np.number]))
st.table(ds)

st.title('Correlation between Component')
option, visualization = st.columns(2)
with option:
    st.subheader('Component to Analyze')
    x_axis = st.selectbox(
        "X Axis",
        ('DASS_21', 'GHQ_12', 'SEC')
    )
    y_axis = st.selectbox(
        "Y Axis",
        ('Appreciation_of_beauty', 'Bravery', 'Creativity', 'Curiosity', 'Fairness', 'Forgiveness', 'Gratitude', 'Honesty', 'Hope', 'Humilty', 'Humor', 'Judgment', 'Kindness', 'Leadership', 'Love', 'Love_of_learning', 'Perseverance', 'Perspective', 'Prudence', 'Self_regulation', 'Social_intelligence', 'Spirituality', 'Teamwork', 'Zest' ,'DASS_21', 'GHQ_12', 'SEC')
    )
    
with visualization:
    st.subheader(x_axis+' - '+y_axis)
    st.altair_chart(alt.Chart(df).mark_square().encode(
        x=x_axis, y=y_axis, color=x_axis
    ))