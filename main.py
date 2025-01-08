import streamlit as st

import random

# 단어 리스트
word_list = [
    '사과', '과일', '일기', '기차', '차례', '례상', '상자', '자전거', '거울', '울타리',
    '타자', '자석', '석유', '유리', '리본', '본능', '능력', '력사', '사람', '람보'
]

# 게임 상태 관리 변수
if 'last_word' not in st.session_state:
    st.session_state.last_word = random.choice(word_list)  # 첫 번째 단어 랜덤으로 선택
    st.session_state.used_words = set([st.session_state.last_word])  # 사용된 단어 추적
    st.session_state.game_over = False  # 게임 종료 여부

def check_valid_word(last_word, new_word):
    """새로 입력한 단어가 끝말잇기 규칙에 맞는지 확인하는 함수"""
    if new_word in word_list and new_word not in st.session_state.used_words:
        if new_word[0] == last_word[-1]:
            return True
    return False

def reset_game():
    """게임 초기화 함수"""
    st.session_state.last_word = random.choice(word_list)
    st.session_state.used_words = set([st.session_state.last_word])
    st.session_state.game_over = False

# 게임 제목
st.title("끝말잇기 게임")

# 게임 종료 시 처리
if st.session_state.game_over:
    st.subheader("게임 종료! 다시 시작하려면 버튼을 눌러주세요.")
    if st.button('새 게임 시작'):
        reset_game()
else:
    # 게임 진행 중
    st.subheader(f"현재 단어: {st.session_state.last_word}")
    user_word = st.text_input("다음 단어를 입력하세요:")

    if user_word:
        if check_valid_word(st.session_state.last_word, user_word):
            st.session_state.used_words.add(user_word)  # 사용된 단어 추가
            st.session_state.last_word = user_word  # 마지막 단어 업데이트
            st.success(f"'{user_word}'가 추가되었습니다!")
        else:
            st.error("입력한 단어가 규칙에 맞지 않거나 이미 사용된 단어입니다!")

    # 게임 오버 조건 (사용자가 단어를 입력하지 못했거나, 규칙에 맞지 않은 단어를 입력했을 때)
    if len(st.session_state.used_words) >= len(word_list):
        st.session_state.game_over = True
        st.error("모든 단어가 사용되었습니다. 게임 종료!")
