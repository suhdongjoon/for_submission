import streamlit as st
import numpy as np
import pandas as pd

st.title("🦾입력한 정보로 분석한 결과 입니다🦾")
st.markdown("---")

st.sidebar.header('Menu')
name = st.sidebar.selectbox('sex', 'hd', ['age', 'bp', 'col', 'hb'])