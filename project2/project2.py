import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from joblib import load
import xgboost


st.sidebar.header('Menu')
age = st.sidebar.slider('나이', 0, 100)
sex = st.sidebar.selectbox('성별', ['남자', '여자'])
gender = True if sex == '남자' else False
hd = st.sidebar.selectbox('심장병', ['심장병 있음', '심장병 없음'])
heart_disease = True if hd == '심장병 있음' else False
bp = st.sidebar.slider('안정혈압', 90, 200)
col = st.sidebar.slider('콜레스테롤', 120, 564)
hb = st.sidebar.slider('최대심박수', 70, 202, None)
btn_clicked = st.sidebar.button("Confirm")

if btn_clicked == True:
    jobs = load("project2/xgb_model.joblib")
    prob = jobs.predict_proba([[age,gender,heart_disease,bp,col,hb]])[:, 1]
    st.write(prob)

    probabilities = []

    for col_val in range(col, 150, -1):
        prob = jobs.predict_proba([[age,gender,heart_disease,bp,col_val,hb]])[:, 1]
        probabilities.append(prob)
    
        if prob < 0.5:
            break


    fig, ax = plt.subplots()
    ax.plot(range(col, col-len(probabilities), -1), probabilities)
    ax.set_xlabel("Cholesterol")
    ax.set_ylabel("Probability of Heart Disease")
    ax.set_title("Probability of Heart Disease by Cholesterol Level")
    st.pyplot(fig)

else:
    st.markdown('<div><a href="https://sparkly-prince-933.notion.site/1ccb865a95e54590bfd61e22b45520fa"><img src="https://i.imgur.com/ktulthH.gif" width=700></a></div>', unsafe_allow_html=True)