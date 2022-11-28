import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Performa Model", page_icon=":bar_chart:", layout="wide")
st.title('Performa Model - HaloFILKOM')

st.header('Model Machine Learning')

df_report_onehot_rf = pd.read_csv('df_report_ml/report_onehot_rf.csv')
df_report_label_rf = pd.read_csv('df_report_ml/report_label_rf.csv')
df_report_label_nb = pd.read_csv('df_report_ml/report_label_nb.csv')
df_report_onehot_knn = pd.read_csv('df_report_ml/report_onehot_knn.csv')
df_report_label_knn = pd.read_csv('df_report_ml/report_label_knn.csv')
df_report_onehot_svm = pd.read_csv('df_report_ml/report_onehot_svm.csv')

st.write('Model Machine Learning yang digunakan adalah Random Forest Classifier, Naive Bayes, K-Nearest Neighbor, dan Support Vector Machine')

st.subheader('Random Forest Classifier - One Hot encoding')
df_presentation_onehot_rf = df_report_onehot_rf.tail(4).reset_index().drop('index',axis=1).rename(columns={'Unnamed: 0':'Metrics'})
st.dataframe(df_presentation_onehot_rf,use_container_width=True)

st.subheader('Random Forest Classifier - Label encoding')
df_presentation_label_rf = df_report_label_rf.tail(3).reset_index().drop('index',axis=1).rename(columns={'Unnamed: 0':'Metrics'})
st.dataframe(df_presentation_label_rf,use_container_width=True)

st.subheader('Naive Bayes - Label encoding')
df_presentation_label_nb = df_report_label_nb.tail(3).reset_index().drop('index',axis=1).rename(columns={'Unnamed: 0':'Metrics'})
st.dataframe(df_presentation_label_nb,use_container_width=True)

st.subheader('K-Nearest Neighbor - One Hot encoding')
df_presentation_onehot_knn = df_report_onehot_knn.tail(4).reset_index().drop('index',axis=1).rename(columns={'Unnamed: 0':'Metrics'})
st.dataframe(df_presentation_onehot_knn,use_container_width=True)

st.subheader('K-Nearest Neighbor - Label encoding')
df_presentation_label_knn = df_report_label_knn.tail(3).reset_index().drop('index',axis=1).rename(columns={'Unnamed: 0':'Metrics'})
st.dataframe(df_presentation_label_knn,use_container_width=True)

st.subheader('Support Vector Machine - Label encoding')
df_presentation_label_svm = df_report_onehot_svm.tail(3).reset_index().drop('index',axis=1).rename(columns={'Unnamed: 0':'Metrics'})
st.dataframe(df_presentation_label_svm,use_container_width=True)


st.header('Model Deep Neural Network')
st.subheader('Plot Akurasi')
st.image('images/model_akurasi.png')
st.subheader('Plot Loss')
st.image('images/model_loss.png')
