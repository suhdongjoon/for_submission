import streamlit as st
import numpy as np
import pandas as pd

st.title("🦾입력한 정보로 분석한 결과 입니다🦾")
st.markdown("---")

st.sidebar.header('Menu')
sex = bool()
name = st.sidebar.selectbox('성별', [sex])






#name = st.sidebar.selectbox('성별', ['sex', 'hd', 'age', 'bp', 'col', 'hb'])