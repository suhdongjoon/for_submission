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
gear = st.markdown('<a href="https://sparkly-prince-933.notion.site/1ccb865a95e54590bfd61e22b45520fa"><img src="https://i.imgur.com/ktulthH.gif" width=800></a>', unsafe_allow_html=True)
btn_clicked1 = st.sidebar.button("Confirm")

if btn_clicked1 == True:
    gear.empty()
    jobs = load("project2/xgb_model.joblib")
    tf = jobs.predict([[age,gender,heart_disease,bp,col,hb]])
    tf_p = jobs.predict_proba([[age,gender,heart_disease,bp,col,hb]])[:, 1]

    st.title("🦾입력한 정보로 분석한 결과 입니다🦾")
    st.markdown("---")


    if tf == 1 : st.write("# 분석 결과 🤦‍♂️ <span style='color:red'>고혈압</span> 🤦‍♂️입니다.", unsafe_allow_html=True)
    if tf == 0 : st.write("# 분석 결과 😊 <span style='color:blue'>정상</span> 😊입니다.", unsafe_allow_html=True)
        
    st.write(f"""
        ## 👇분석 결과👇
        ### 👉 성별 : {sex}
        ### 👉 나이 : {age}세
        ### 👉 심장병(有, 無) : {hd}
        ### 👉 혈압 : {bp}mmHg
        ### 👉 콜레스트롤 : {col}TC
        ### 👉 심박수 : {hb}bpm
    """)
    st.write(f"""
    ## 결과에 실망하지 마세요😭
    ### 👇확률을 알려드립니다👇
    ### 👉 {', '.join([f'{p*100:.4f}%' for p in tf_p])}
    """)
btn_clicked2 = st.button("Next")

if btn_clicked2 == True and tf == 1:
    jobs = load("project2/xgb_model.joblib")    
    probabilities = []
    for col_val in range(col, 150, -1):
        tf_p = jobs.predict_proba([[age,gender,heart_disease,bp,col_val,hb]])[:, 1]
        probabilities.append(tf_p)
        if tf_p < 0.5:
            break


    fig, ax = plt.subplots()
    ax.plot(range(col, col-len(probabilities), -1), probabilities)
    ax.set_xlabel("Cholesterol")
    ax.set_ylabel("Probability of Heart Disease")
    ax.set_title("Probability of Heart Disease by Cholesterol Level")
    st.pyplot(fig)
    gear.empty()