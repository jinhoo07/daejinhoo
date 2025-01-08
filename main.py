import random

# 단어 리스트 (필요에 따라 추가하거나 변경할 수 있습니다)
word_list = [
    '사과', '과일', '일기', '기차', '차례', '례상', '상자', '자전거', '거울', '울타리',
    '타자', '자석', '석유', '유리', '리본', '본능', '능력', '력사', '사람', '람보'
]

def check_valid_word(last_word, new_word):
    """새로 입력한 단어가 끝말잇기 규칙에 맞는지 확인하는 함수"""
    if new_word in word_list:
        if new_word[0] == last_word[-1]:
            return True
        else:
            print(f"새 단어 '{new_word}'는 이전 단어 '{last_word}'의 끝 글자 '{last_word[-1]}'와 맞지 않습니다.")
            return False
    else:
        print(f"'{new_word}'는 유효한 단어 목록에 없습니다.")
        return False

def end_game():
    """게임 종료 함수"""
    print("게임이 종료되었습니다!")
    exit()

def play_game():
    """끝말잇기 게임을 진행하는 함수"""
    print("끝말잇기 게임을 시작합니다!")
    print("게임 규칙: 이전 단어의 마지막 글자로 시작하는 단어를 입력해주세요.")
    print("끝내려면 '종료'라고 입력하세요.")
    
    # 게임의 첫 단어를 랜덤으로 고릅니다.
    last_word = random.choice(word_list)
    print(f"첫 단어는 '{last_word}'입니다.")
    
    while True:
        new_word = input(f"'{last_word}'에 이어서 단어를 입력하세요: ").strip()
        
        # 게임 종료 조건
        if new_word == '종료':
            end_game()

        # 새 단어가 규칙에 맞는지 확인
        if check_valid_word(last_word, new_word):
            last_word = new_word
        else:
            print("다시 입력해주세요.")

# 게임 실행
play_game()
