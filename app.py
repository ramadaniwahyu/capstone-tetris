import altair as alt
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

df = pd.read_csv('dataset.csv')

df['Participant'] = df['Participant'].astype(str)
df['Sons'] = df['Sons'].astype(str)

# page_title="""
# <head>
# <title>Manusia dan Covid-19 | Dicky Wahyu Ramadani </title>
# </head>
# """

# st.markdown(page_title)

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
-   Values in Action Inventory of Strengths-120 (VIA-IS-120) yang digunakan untuk mengukur kekuatan karakter (Character Strength). Bisa dibaca lebih lanjut [disini](https://www.viacharacter.org/character-strengths);
-   Depression, Anxiety, and Stress Scales-21 (DASS-21) yang digunakan untuk mengukur tingkat stress, depresi dan kecemasan yang dirasakan selama masa pandemi. Semakin tinggi skor mengindikasikan semakin tinggi tingkat stress yang dialami;
-   General Health Questionnaire-12 (GHQ-12) digunakan untuk mengukur kesehatan psikologis secara umum. Semakin tinggi skor mengindikasikan semakin buruk kesehatan mental;
-   dan yang terakhir, Self-efficacy measure for Covid-19 (SEC), digunakan untuk mengukur kepercayaan terhadap diri sendiri untuk mengatasi hal-hal dalam kehidupan sehari-hari selama masa pandemi. Semakin tinggi skor mengindikasikan semakin tinggi rasa percaya diri yang dimiliki.
    """
)

st.header('Sebaran data')
st.subheader('Korelasi Antar Komponen')
axis = ['Appreciation_of_beauty', 'Bravery', 'Creativity', 'Curiosity', 'Fairness', 'Forgiveness', 'Gratitude', 'Honesty', 'Hope', 'Humilty', 'Humor', 'Judgment', 'Kindness', 'Leadership', 'Love', 'Love_of_learning', 'Perseverance', 'Perspective', 'Prudence', 'Self_regulation', 'Social_intelligence', 'Spirituality', 'Teamwork', 'Zest' ]
dd = df.corr().loc[axis, ['DASS_21', 'GHQ_12', 'SEC']]
st.line_chart(dd)

st.markdown("""Dari diagram diatas dapat terlihat korelasi antara Kekuatan Karakter dengan DASS_21 dan GHQ_12 yang menunjukkan tren negatif, dan korelasi dengan SEC yang menunjukkan tren positif.<br /><br />
            Diantara ke-24 Kekuatan Karakter yang memberikan koefisien terbesar adalah sebagai berikut:
            """, unsafe_allow_html=True)

via1, via2, via3, via4 = st.columns(4)
via5, via6, via7, via8 = st.columns(4)
with via1:
    st. markdown("""
                 <div style='text-align: center;'>
                 <a href='https://viacharacter.org/character-strengths/zest'><img width=250 src='https://ramadani.my.id/capstone-tetris/img/zest.png'/></a>
                 <p><i>"Antusiasme, menjalani hidup dengan penuh semangat dan mampu memberikan semangat ke orang lain"</i></p>
                 </div>
                 """, unsafe_allow_html=True)
with via2:
    st. markdown("""
                 <div style='text-align: center;'>
                 <a href='https://viacharacter.org/character-strengths/hope'><img width=250 src='https://ramadani.my.id/capstone-tetris/img/hope.png'/></a>
                 <p><i>Optimisme, mengharapkan yang terbaik untuk masa depan, percaya akan diri sendiri atas segala tindakan dan semua akan berjalan dengan baik</i></p>
                 </div>
                 """, unsafe_allow_html=True)
with via3:
    st. markdown("""
                 <div style='text-align: center;'>
                 <a href='https://viacharacter.org/character-strengths/perseverance'><img width=250 src='https://ramadani.my.id/capstone-tetris/img/persev.png'/></a>
                 <p><i>"Tetap bertahan untuk menuju tujuan meskipun aral melintang dan banyak halangan yang menghadang"</i></p>
                 </div>
                 """, unsafe_allow_html=True)
with via4:
    st. markdown("""
                 <div style='text-align: center;'>
                 <a href='https://viacharacter.org/character-strengths/gratitude'><img width=250 src='https://ramadani.my.id/capstone-tetris/img/grat.png'/></a>
                 <p><i>"Bersyukur atas segala sesuatu dan menunjukkannya kepada orang lain"</i></p>
                 </div>
                 """, unsafe_allow_html=True)
with via5:
    st. markdown("""
                 <div style='text-align: center;'>
                 <a href='https://viacharacter.org/character-strengths/curiosity'><img width=250 src='https://ramadani.my.id/capstone-tetris/img/curio.png'/></a>
                 <p><i>"Rasa penasaran untuk mendapatkan pengalaman baru tanpa menghalangi kepentingan diri dan orang lain saat ini"</i></p>
                 </div>
                 """, unsafe_allow_html=True)
with via6:
    st. markdown("""
                 <div style='text-align: center;'>
                 <a href='https://viacharacter.org/character-strengths/love'><img width=250 src='https://ramadani.my.id/capstone-tetris/img/love.png'/></a>
                 <p><i>"Menjalani suatu hubungan yang hangat, peduli untuk saling memberi dan menerima satu sama lain"</i></p>
                 </div>
                 """, unsafe_allow_html=True)
with via7:
    st. markdown("""
                 <div style='text-align: center;'>
                 <a href='https://viacharacter.org/character-strengths/spirituality'><img width=250 src='https://ramadani.my.id/capstone-tetris/img/spirit.png'/></a>
                 <p><i>"Merasakan dan memahami tujuan hidup sehari-hari, serta mampu melihat diri sendiri dalam skema besar dunia ini"</i></p>
                 </div>
                 """, unsafe_allow_html=True)
with via8:
    st. markdown("""
                 <div style='text-align: center;'>
                 <a href='https://viacharacter.org/character-strengths/self-regulation'><img width=250 src='https://ramadani.my.id/capstone-tetris/img/selfreg.png'/><a/>
                 <p><i>"Mengatur perasaan, emosi, dan tindakan serta disiplin dan terkendali"<i/></p>
                 </div>
                 """, unsafe_allow_html=True)

st.subheader('Komponen')
option, set1 = st.columns(2)
visualization1, visualization2, visualization3 = st.columns(3)
with option:
    y_axis = st.selectbox(
        "Pilih komponen",
        ('Appreciation_of_beauty', 'Bravery', 'Creativity', 'Curiosity', 'Fairness', 'Forgiveness', 'Gratitude', 'Honesty', 'Hope', 'Humilty', 'Humor', 'Judgment', 'Kindness', 'Leadership', 'Love', 'Love_of_learning', 'Perseverance', 'Perspective', 'Prudence', 'Self_regulation', 'Social_intelligence', 'Spirituality', 'Teamwork', 'Zest' ,'DASS_21', 'GHQ_12', 'SEC')
    )

with set1:
    st.write('Silahkan perhatikan koefisien korelasi dibawah ini')
    dd = df.corr().loc[y_axis, ['DASS_21', 'GHQ_12', 'SEC']]
    st.table(dd)
with visualization1:
    st.markdown("<h3 style='text-align: center; color: blue;'>DASS_21</h3>", unsafe_allow_html=True)
    st.altair_chart(
        alt.Chart(df.reset_index())
        .mark_point(color='blue')
        .encode(y=y_axis, x='DASS_21'),
        use_container_width=False
    )

with visualization2:
    st.markdown("<h3 style='text-align: center; color: red;'>GHQ_12</h3>", unsafe_allow_html=True)
    st.altair_chart(
        alt.Chart(df.reset_index())
        .mark_circle(color='red')
        .encode(y=y_axis, x='GHQ_12'),
        use_container_width=False
    )
    
with visualization3:
    st.markdown("<h3 style='text-align: center; color: yellow;'>SEC</h3>", unsafe_allow_html=True)
    st.altair_chart(
        alt.Chart(df.reset_index())
        .mark_square(color='yellow')
        .encode(y=y_axis, x='SEC'),
        use_container_width=False
    )

st.header('Summary')
st.markdown(
            """
Kesimpulan yang dapat diambil dari diagram diatas adalah sebagai berikut:
- Terdapat korelasi samar negatif antara tekanan psikologis yang dirasakan, psikologis kesehatan secara umum dengan Kekuatan Karakter pada saat pandemi. Semakin rendah tekanan psikologis dan psikologis kesehatan yang dirasakan, maka kekuatan karakter yang dimiliki akan semakin tinggi
- Sedangkan korelasi samar positif muncul antara Efikasi Diri selama pandemi dengan kekuatan karakter secara umum. Semakin tinggi efikasi diri, maka semakin baik karakter yang dimiliki.
-   Korelasi samar ini mengindikasikan bahwa tekanan psikologis, psikologis kesehatan secara umum, dan efikasi diri ini tidak memiliki pengaruh yang kuat terhadap perubahan Kekuatan Karakter.
-   Zest, Hope, Perseverance, Gratitude, Curiosity, Love, Spirituality, dan Self Regulation merupakan karakter yang perlu dikembangkan karena karakter tersebut dapat memberikan kontribusi positif untuk menjalani masa pandemi ini.
""")



# st.image('https://ramadani.my.id/capstone-tetris/footer.jpg')

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