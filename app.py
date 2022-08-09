import streamlit as st
import joblib

#load the joblib model
model_nb=joblit.load('spam-ham')

st.title('SPAM-HAM CLASSIFIER')
ip = st.text_input('Enter the text:')

op = model_nb.predict([ip])
if st.button('Predict'):
  st.title(op[0])
  
  
  
  
  
