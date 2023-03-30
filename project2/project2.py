import streamlit as st
import numpy as np
import pandas as pd
from joblib import load
import xgboost


st.title("🦾입력한 정보로 분석한 결과 입니다🦾")
st.markdown("---")

st.sidebar.header('Menu')
age = st.sidebar.slider('나이', 0, 100)

options = ['남자', '여자']
sex = st.sidebar.checkbox('성별', options)



options2 = ['심장병 있음', '심장병 없음']
hd = st.sidebar.checkbox('심장병', options2)




bp = st.sidebar.slider('안정혈압', 90, 200)
col = st.sidebar.slider('콜레스테롤', 120, 564)
hb = st.sidebar.slider('최대심박수', 70, 202)

jobs = load("project2/xgb_model.joblib")
prob = jobs.predict_proba([[age,sex,hd,bp,col,hb]])[:, 1]
st.write(prob)


