import streamlit as st
import pandas as pd
#import openpyxl

st.title("MARI KITA LIHAT KESEHATAN DI YOGYAKARTA")

st.markdown('Streamlit apps by [Ahmad Putra](https://github.com/ahmad-putra)')

dataset = pd.read_csv('jenis_penyakit.csv')
dataset

st.caption('(*) Data sementara')

st.markdown('**Apa makna dari kesehatan ?**\
    Mengutip dari pernyataan [**Kemkes RI**](https://pusatkrisis.kemkes.go.id/mengenal-makna-kesehatan),\
    Mengacu pada Undang – Undang nomor 36 tahun 2009 tentang kesehatan,\
    sehat didefinisikan sebagai suatu keadaan sehat baik secara fisik, mental, spiritual maupun sosial\
    yang memungkinkan setiap orang untuk hidup produktif secara sosial dan ekonomis.\
    **Berangkat dari pengertian diatas, dapat diketahui bahwa kesehatan merupakan hal yang luas dan bukan hanya kesehatan secara fisik.**')