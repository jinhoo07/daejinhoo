import streamlit as st

st.title("나의 첫번째 앱")

st.write("안녕하세요. 저는 ❤️입니다")
st.write("저의 이메일 주소 : 23_10808.daejin.sen.hs.kr")


import streamlit as st
import random

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write(random.ranint(1,999)
else:
    st.write("Goodbye")
    
import streamlit as st

on = st.toggle("Activate feature")

if on:
    st.write("Feature activated!")

