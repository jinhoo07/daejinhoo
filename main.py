import streamlit as st

import random
# 이전에 입력된 단어들을 저장할 리스트
words = []

# 게임의 시작 메시지
st.title("끝말잇기 게임")
st.write("끝말잇기 게임에 오신 것을 환영합니다! 처음 단어를 입력해주세요.")

# 단어 입력 받기
user_input = st.text_input("단어를 입력하세요:")

if user_input:
    # 단어가 게임 규칙에 맞는지 확인
    if len(words) == 0:  # 첫 번째 단어인 경우
        words.append(user_input)
        st.write(f"첫 번째 단어: {user_input}")
    else:
        last_word = words[-1]
        # 이전 단어의 마지막 글자와 현재 입력된 단어의 첫 글자 비교
        if user_input[0] == last_word[-1]:
            words.append(user_input)
            st.write(f"잘했어요! 다음 단어는 '{user_input}' 입니다.")
        else:
            st.write(f"오류! '{last_word[-1]}'로 시작하는 단어를 입력해야 합니다.")
else:
    st.write("단어를 입력해주세요.")
    
# 게임 진행 상황을 보여주기
if len(words) > 0:
    st.write("현재까지 입력된 단어들:")
    st.write(" → ".join(words))

   
       
