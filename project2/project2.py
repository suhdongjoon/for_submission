import streamlit as st
import numpy as np
import pandas as pd

st.title("🦾입력한 정보로 분석한 결과 입니다🦾")
st.markdown("---")

st.sidebar.header('Menu')
int(age) = st.sidebar.selectbox('나이', [True, False])
sex = st.sidebar.selectbox('성별', [])
hd = st.sidebar.selectbox('심장병', [True, False])
bp = st.sidebar.selectbox('안정혈압', [])
col = st.sidebar.selectbox('콜레스테롤', [])
hb = st.sidebar.selectbox('최대심박수', [])






#name = st.sidebar.selectbox('성별', ['sex', 'hd', 'age', 'bp', 'col', 'hb'])