import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components

st.set_page_config(page_title="Chatbot Filkom", page_icon=":bar_chart:", layout="wide")
st.title('HaloFILKOM')

components.iframe("https://s.ub.ac.id/filkombot", height=500)

