import streamlit as st
import pandas as pd
#import openpyxl

st.title("MARI KITA LIHAT KESEHATAN DI YOGYAKARTA")

st.markdown('Streamlit apps by [Ahmad Putra](https://github.com/ahmad-putra)')

dataset = pd.read_csv('jenis_penyakit.csv')
dataset

st.caption('(*) Data sementara')