import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Hyperparemeter Tuning", page_icon=":bar_chart:", layout="wide")
st.title('Hyperparemeter Tuning - HaloFILKOM')

st.header('Model')
st.write('Model yang digunakan adalah deep neural network')

st.header('Hyperparameter Tuning')
st.subheader('Plot Hyperparameter')
st.image('images/hyperparameter_plot.png')

st.subheader('Batch Accuracy')
st.image('images/batch_accuracy.png')

st.subheader('Batch Loss')
st.image('images/batch_loss.png')

st.subheader('Hasil Eksperimen')
df = pd.read_csv('hparams_table.csv', delimiter=',')
st.dataframe(df,use_container_width=True)
