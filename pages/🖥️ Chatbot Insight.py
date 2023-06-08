import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

import requests

st.set_page_config(page_title="Analisa Chatbot", page_icon=":bar_chart:", layout="wide")
st.title('Analisa Chatbot - HaloFILKOM')

# setup api
endpoint = 'https://filkombotapi.emwrks.com/api.php?sql='

st.subheader('Log Seluruh Pertanyaan')
sql = "SELECT tag FROM log_chatbot group by tag"
r = requests.get(endpoint + sql)
decoded = r.json()
df_tag = pd.DataFrame(decoded)
tag = st.selectbox('Pilih Tag', ["Semua Tag"] + df_tag['tag'].tolist())
if tag == "Semua Tag":
    sql = "SELECT waktu,pertanyaan,tag FROM log_chatbot"
else: 
    sql = "SELECT waktu,pertanyaan,tag FROM log_chatbot WHERE tag = '{}'".format(tag)

# get data from api
r = requests.get(endpoint + sql)
decoded = r.json()
df = pd.DataFrame(decoded)

st.dataframe(df)

st.subheader('Persebaran Kategori Pertanyaan')
sql = "SELECT tag, COUNT(*) as jumlah  FROM log_chatbot GROUP BY tag ;"

r = requests.get(endpoint + sql)
decoded = r.json()
df = pd.DataFrame(decoded)
df['jumlah'] = df['jumlah'].astype(int)
df = df.sort_values(by='jumlah', ascending=False)

fig = alt.Chart(df).mark_bar().encode(
    x='tag',
    y='jumlah',
    color='tag'
).properties(
    width=alt.Step(80)  # controls width of bar.
).interactive()

st.altair_chart(fig, use_container_width=True)

st.subheader('Jumlah Pertanyaan per Tag')
sql = "SELECT CAST(waktu as date) as tanggal, COUNT(*) as jumlah, tag  from log_chatbot group by tanggal, tag ORDER BY tanggal;"

r = requests.get(endpoint + sql)
decoded = r.json()
df = pd.DataFrame(decoded)

# make stacked bar chart
fig = alt.Chart(df).mark_bar(size=80).encode(
    alt.X('tanggal:T', title='Tanggal', axis=alt.Axis(format='%d %b %Y')),
    alt.Y('jumlah:Q', title='Jumlah'),
    color='tag'
).configure_axis(
    grid=False,
).interactive()

st.altair_chart(fig, use_container_width=True)