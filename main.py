import streamlit as st
import pandas as pd
#import openpyxl

st.title("MARI KITA LIHAT KESEHATAN DI YOGYAKARTA")

st.markdown('Streamlit apps by [Ahmad Putra](https://github.com/ahmad-putra)')

dataset = pd.read_csv('Daerah_diy-jumlah-kasus-penyakit-pada-manusia-2018-2022.csv')
dataset

st.caption('(*) Data sementara')

st.markdown('**Apa makna dari kesehatan ?**\
    Mengutip dari pernyataan [**Kemkes RI**](https://pusatkrisis.kemkes.go.id/mengenal-makna-kesehatan),\
    Mengacu pada Undang – Undang nomor 36 tahun 2009 tentang kesehatan,\
    sehat didefinisikan sebagai suatu keadaan sehat baik secara fisik, mental, spiritual maupun sosial\
    yang memungkinkan setiap orang untuk hidup produktif secara sosial dan ekonomis.\
    **Berangkat dari pengertian diatas, dapat diketahui bahwa kesehatan merupakan hal yang luas dan bukan hanya kesehatan secara fisik.**')

st.markdown('Mari kita lihat, **Bagaimana pesebaran penyakit di berbagai kabupaten/kota di Yogyakarta ?**')

sleman, kota, = st.columns(2)
with sleman:
   st.subheader("Kabupaten Sleman")
   data_sleman = pd.read_csv('Daerah_kab-sleman-jumlah-kasus-penyakit-pada-manusia-2018-2022.csv')
   st.dataframe(data_sleman)

with kota:
   st.subheader("Kota Yogyakarta")
   data_kota = pd.read_csv('Daerah_kota-yogyakarta-jumlah-kasus-penyakit-pada-manusia-2018-2022.csv')
   st.dataframe(data_kota)

bantul, kulonprogo, = st.columns(2)
with bantul:
   st.subheader("Kabupaten Bantul")
   data_bantul = pd.read_csv('Daerah_kab-bantul-jumlah-kasus-penyakit-pada-manusia-2018-2022.csv')
   st.dataframe(data_bantul)

with kulonprogo:
   st.subheader("Kabupaten Kulonprogo")
   data_kulonprogo = pd.read_csv('Daerah_kab-kulon-progo-jumlah-kasus-penyakit-pada-manusia-2018-2022.csv')
   st.dataframe(data_kulonprogo)