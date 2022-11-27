import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import MySQLdb

st.set_page_config(page_title="Analisa Chatbot", page_icon=":bar_chart:", layout="wide")
st.title('Analisa Chatbot - HaloFILKOM')

# setup database
db = MySQLdb.connect(host="db-mysql-sgp1-73465-do-user-12035841-0.b.db.ondigitalocean.com", 
                    user="doadmin", 
                    passwd="AVNS_1GNQHAtlxYOkhNeywGX", 
                    db="filkombot",
                    port=25060,
                    ssl={'ca': 'ca-certificate.crt'})

st.subheader('Log Seluruh Pertanyaan')
sql = "SELECT tag FROM log_chatbot group by tag"
df_tag = pd.read_sql(sql, db)
tag = st.selectbox('Pilih Tag', ["Semua Tag"] + df_tag['tag'].tolist())
if tag == "Semua Tag":
    sql = "SELECT waktu,pertanyaan,tag FROM log_chatbot"
else: 
    sql = "SELECT waktu,pertanyaan,tag FROM log_chatbot WHERE tag = '{}'".format(tag)
df = pd.read_sql(sql, db)
st.dataframe(df)

st.subheader('Persebaran Kategori Pertanyaan')
sql = "SELECT tag, COUNT(*) as jumlah  FROM log_chatbot GROUP BY tag ;"
df = pd.read_sql(sql, db)
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
df = pd.read_sql(sql, db)
# make stacked bar chart
fig = alt.Chart(df).mark_bar(size=80).encode(
    alt.X('tanggal:T', title='Tanggal', axis=alt.Axis(format='%d %b %Y')),
    y='jumlah',
    color='tag'
).configure_axis(
    grid=False,
).interactive()

st.altair_chart(fig, use_container_width=True)