import streamlit as st
import numpy as np
import pandas as pd

st.title("🦾입력한 정보로 분석한 결과 입니다🦾")
st.markdown("---")

st.sidebar.header('Menu')
age = st.slider('나이', '0','100')
sex = st.sidebar.selectbox('성별', [True, False])
hd = st.sidebar.selectbox('심장병', [True, False])
bp = st.slider('안정혈압', '90', '200')
col = st.slider('콜레스테롤', '120', '564')
hb = st.slider('최대심박수', '70', '202')






#name = st.sidebar.selectbox('성별', ['sex', 'hd', 'age', 'bp', 'col', 'hb'])