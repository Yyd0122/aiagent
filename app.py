# 분류 모델 웹앱 만들기

import streamlit as st

# 1. 기계학습 모델 파일 로드
import joblib

model = joblib.load('linear_regression_model.pkl')

# 2. 모델 설명
st.title('작물수확량 예측 에이전트')

st.subheader('모델 설명')

st.write(' - 기계학습 알고리즘 : 로지스틱 회귀 ')

st.write(' - 학습 데이터 출처 : https://www.kaggle.com/')

st.write(' - 훈련    데이터 : 7000개')

st.write(' - 테스트 데이터 : 3000개')

st.write(' - 인공지능 모델 정확도 : -0.0')

# 3.데이터 시각화

col1, col2, col3 = st.columns(3)  

with col1:

      st.subheader('데이터시각화1')

      st.image('시각화1 (1).png' )   # 이미지 불러오기

with col2:

      st.subheader('데이터시각화2')

      st.image('시각화2 (1).png' )   # 이미지 불러오기

with col3:

      st.subheader('데이터시각화3')

      st.image('시각화3.png' )   # 이미지 불러오기


# 4.모델 활용

st.subheader('모델 활용')

st.write('**** 다음을 입력하세요.. 인공지능이 작물수확량을 알려드립니다! (입력한 데이터는 외부에 공개되지 않습니다) ')

a = st.number_input(' 살충제사용량 입력(kg per HA) ', value=0)      #초기값은 0

b = st.number_input(' 비료사용량 입력(kg per HA) ', value=0)     # 초기값은 0



if st.button('작물수확량 예측'):            # 사용자가 '작물수확량 예측' 버튼을 누르면

        input_data = [[a,b]]     # 사용자가 입력한 a,b 를 input_data에 저장하고

        p = model.predict(input_data)         # model이 예측한 값을 p에 저장한다

        st.write('인공지능의 예측 작물수확량은(MT per HA)', p)



