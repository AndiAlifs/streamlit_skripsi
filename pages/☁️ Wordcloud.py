import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from wordcloud import WordCloud
from textwrap import wrap
import matplotlib.pyplot as plt

st.set_page_config(page_title="Analisa Wordcloud", page_icon=":bar_chart:", layout="wide")

st.title('Analisa Wordcloud - HaloFILKOM')

df_dtm = pd.read_csv('df_dtm_intent.csv')
df_dtm = df_dtm.set_index(['tag'])
tag = st.selectbox('Pilih Tag', ["Semua"] + df_dtm.index.tolist())

if tag == "Semua":
    df_dtm
else:
    data = df_dtm[df_dtm.index==tag]
    st.write(data)

    st.subheader('Wordcloud untuk tag '+ tag)
    dataForWordCloud = data.iloc[0].transpose().sort_values(ascending=False)

    # Function for generating word clouds
    def generate_wordcloud(data,title):
        wc = WordCloud(max_words=150).generate_from_frequencies(data)
        plt.figure(figsize=(10,8))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis("off")
        plt.title('\n'.join(wrap(title,60)),fontsize=13)
        plt.show()
        st.pyplot(plt)

    # create wordcloud
    generate_wordcloud(dataForWordCloud,tag)
