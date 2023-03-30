import streamlit as st
import numpy as np
import pandas as pd
pip install joblib
import joblib


st.title("🦾입력한 정보로 분석한 결과 입니다🦾")
st.markdown("---")

st.sidebar.header('Menu')
age = st.sidebar.slider('나이', 0, 100)
sex = st.sidebar.selectbox('성별', [True, False])
hd = st.sidebar.selectbox('심장병', [True, False])
bp = st.sidebar.slider('안정혈압', 90, 200)
col = st.sidebar.slider('콜레스테롤', 120, 564)
hb = st.sidebar.slider('최대심박수', 70, 202)

import os
st.write(os.getcwd())







#name = st.sidebar.selectbox('성별', ['sex', 'hd', 'age', 'bp', 'col', 'hb'])