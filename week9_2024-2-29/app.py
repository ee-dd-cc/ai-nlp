# app.py
import pickle
import streamlit as st
from PIL import Image

pickle_in = open('week9_2024-2-29/model_iris copy.pkl', 'rb')
classifier = pickle.load(pickle_in)

# print('----classifier', classifier)

def predic(sepal_length, sepal_width, pepal_length, pepal_width):
  prediction = classifier.predict([[sepal_length, sepal_width, pepal_length, pepal_width]])
  print(prediction)
  return prediction

def Input_Output():
  st.title('my title')
  st.image('https://imgs.gvm.com.tw/upload/gallery/20221204/125075.jpg')
  st.markdown('you are using st', unsafe_allow_html=True)
  sepal_length = st.text_input('enter sp length', '.')
  sepal_width = st.text_input('enter sp width', '.')
  pepal_length = st.text_input('enter p length', '.')
  pepal_width = st.text_input('enter p width', '.')
  
  result = ''
  if st.button('click here to Predict'):
    result = predic(sepal_length, sepal_width, pepal_length, pepal_width)
    st.balloons()

  st.success('The output is {}'.format(result))

Input_Output()