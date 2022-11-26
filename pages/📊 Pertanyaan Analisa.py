import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Pertanyaan Analisa", page_icon=":bar_chart:", layout="wide")

st.title('Analisa Pertanyaan - HaloFILKOM')

st.header('Pertanyaan')
dfPertanyaan = pd.read_csv('dfPertanyaan.csv')

listTopik= ["SEMUA TOPIK"]+ dfPertanyaan['topik'].unique().tolist()

topik = st.selectbox('Pilih Topik', listTopik)

if topik == "SEMUA TOPIK":
    dfPertanyaan
else:
    dfPertanyaan[dfPertanyaan['topik']==topik]


st.header('Persebaran Jawaban')
dfPersebaran = dfPertanyaan['topik'].value_counts()
topNum = st.slider('Pilih Jumlah Jawaban', min_value=1, max_value=len(dfPersebaran), value=5, step=1)
dfPersebaran = dfPertanyaan['topik'].value_counts().head(topNum).reset_index(name='jumlah')
st.bar_chart(dfPersebaran)