import altair as alt
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

st.set_page_config(layout="wide")

df = pd.read_csv('dataset.csv')

df['Participant'] = df['Participant'].astype(str)
df['Sons'] = df['Sons'].astype(str)

header="""<style>
.header {
background-image: url('https://ramadani.my.id/capstone-tetris/header.jpg');
background-size: cover; /* Resize the background image to cover the entire container */
text-align: center;
}
</style>
<div class="header">
<img src='https://ramadani.my.id/capstone-tetris/header.jpg'/>
</div>
"""
st.markdown(header,unsafe_allow_html=True)

st.title('Manusia dan Pandemi Covid-19')
col1, mid, col2 = st.columns([1,1,40])
with col1:
    st.image('profpic.png', width=50)
with col2:
    st.write('[Dicky Wahyu Ramadani](https://wa.me/628113502605) - TETRIS PROA - Oktober 2022')

st.header('Pendahuluan')
st.write(
    'Pandemi Covid-19 telah membuat banyak orang di dunia ini merasakan tekanan psikologis yang berat mulai dari sulitnya berinteraksi dengan keluarga, teman, tetangga dan banyak orang lainnya, belum lagi apabila harus menjalani masa isolasi yang dapat memberikan tekanan yang sangat berat bagi manusia sebagai mahluk sosial. Lalu bagaimana dampaknya terhadap kita sebagai manusia?'
    )

st.write(
    'Data yang digunakan diambil dari [sini](https://figshare.com/articles/dataset/Covid-19_and_Character_Strengths/12366494). Data ini merupakan hasil survey yang dilaksanakan terhadap participant dengan karakteristik sebagai berikut:'
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

st.markdown(
    """Data ini diambil dengan cara penyebaran kuesioner yang berisikan beberapa materi antara lain:
-   Values in Action Inventory of Strengths-120 (VIA-IS-120) yang digunakan untuk mengukur kekuatan karakter (Character Strength);
-   Depression, Anxiety, and Stress Scales-21 (DASS-21) yang digunakan untuk mengukur tingkat stress, depresi dan kecemasan yang dirasakan selama masa pandemi. Semakin tinggi skor mengindikasikan semakin tinggi tingkat stress yang dialami;
-   General Health Questionnaire-12 (GHQ-12) digunakan untuk mengukur kesehatan psikologis secara umum. Semakin tinggi skor mengindikasikan semakin buruk kesehatan mental;
-   dan yang terakhir, Self-efficacy measure for Covid-19 (SEC), digunakan untuk mengukur kepercayaan terhadap diri sendiri untuk mengatasi hal-hal dalam kehidupan sehari-hari selama masa pandemi. Semakin tinggi skor mengindikasikan semakin tinggi rasa percaya diri yang dimiliki.
    """
)

st.header('Sebaran data')
option, visualization = st.columns(2)
with option:
    st.subheader('Komponen')
    y_axis = st.selectbox(
        "Pilih komponen",
        ('Appreciation_of_beauty', 'Bravery', 'Creativity', 'Curiosity', 'Fairness', 'Forgiveness', 'Gratitude', 'Honesty', 'Hope', 'Humilty', 'Humor', 'Judgment', 'Kindness', 'Leadership', 'Love', 'Love_of_learning', 'Perseverance', 'Perspective', 'Prudence', 'Self_regulation', 'Social_intelligence', 'Spirituality', 'Teamwork', 'Zest' ,'DASS_21', 'GHQ_12', 'SEC')
    )
    
    
    # legend="""
    # <style>
    #     .dot {
    #     height: 25px;
    #     width: 25px;
    #     border-radius: 50%;
    #     display: inline-block;
    #     margin: auto;
    #     }
    # </style>
    # <div>
    #     <span class="dot" style='background-color: blue'></span>DASS_21&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    #     <span class="dot" style='background-color: red'></span>GHQ_12&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    #     <span class="dot" style='background-color: yellow'></span>SEC
    # </div>
    # """
    # st.markdown(legend, unsafe_allow_html=True)

# base = alt.Chart(df.reset_index()).encode(y=y_axis)

# c = alt.layer(
#     base.mark_point(color='blue').encode(x='DASS_21'),
#     base.mark_circle(color='red').encode(x='GHQ_12'),
#     base.mark_square(color='yellow').encode(x='SEC')
# )
with visualization:
    st.subheader(y_axis)
    st.altair_chart(
        alt.Chart(df.reset_index())
        .mark_point(color='blue')
        .encode(y=y_axis, x='DASS_21'),
        use_container_width=False
    )
    st.altair_chart(
        alt.Chart(df.reset_index())
        .mark_circle(color='red')
        .encode(y=y_axis, x='GHQ_12'),
        use_container_width=False
    )
    st.altair_chart(
        alt.Chart(df.reset_index())
        .mark_square(color='yellow')
        .encode(y=y_axis, x='SEC'),
        use_container_width=False
    )


# st.write(
#     'Diagram diatas memperlihatkan sebaran data antara Character Strength dalam VIA-IS-120 dengan parameter DASS_21 yang menunju'
# )

st.header('Summary')
st.markdown(
            """
Kesimpulan yang dapat diambil dari diagram diatas adalah sebagai berikut:
- Terdapat korelasi samar negatif antara tekanan psikologis yang dirasakan, psikologis kesehatan secara umum dengan Kekuatan Karakter pada saat pandemi. Semakin rendah tekanan psikologis dan psikologis kesehatan yang dirasakan, maka kekuatan karakter yang dimiliki akan semakin tinggi
- Sedangkan korelasi samar positif muncul antara Efikasi Diri selama pandemi dengan kekuatan karakter secara umum. Semakin tinggi efikasi diri, maka semakin baik karakter yang dimiliki.
""")

st.header('Jadi, bagaimana dengan kondisi di Indonesia pada khususnya?')
st.write('Sampai saat ini belum ada studi ilmiah tentang ini.')

st.image('https://ramadani.my.id/capstone-tetris/footer.jpg')

footer="""<style>
a:link , a:visited{
color: #9EA25D;
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: black;
background-color: transparent;
text-decoration: none;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #615DA2;
color: #9EA25D;
text-align: center;
}
</style>
<div class="footer">
<p>Developed by <a style='display: block; text-align: center;' href="https://ramadani.my.id/" target="_blank">Dicky Wahyu Ramadani</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)