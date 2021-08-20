# Section 13-1
# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본 완성

import random
import time
# 사운드 출력 필요 모듈
import pygame
import sqlite3
import datetime

# DB 생성 & Auto Commit
# 본인 DB 경로
conn = sqlite3.connect('/Users/yoonseo/Desktop/python/python_basic/resource/records.db', isolation_level=None)

# Cursor
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT, cor_cnt INTEGER, record text, regdate text)")

words = []      # 영어 단어 리스트 1000개
n = 1           # 게임 시도 횟수
cor_cnt = 0     # 정답 개수

with open('/Users/yoonseo/Desktop/python/python_basic/resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())   # 양쪽 공백 제거
# print(words)    # 단어 리스트 확인

input("Ready? Press Enter Key!") # 게임 시작

start = time.time()

while n <= 5:
    random.shuffle(words)    # 임의로 순서 섞기
    q = random.choice(words)
    print()

    print("*Quiz # {}".format(n))
    print(q)   # 문제 출력

    x = input()   # 타이핑 입력
    print()

    if str(q).strip() == str(x).strip():  # 입력 확인 (공백 제거)
        print("Pass!")
        # 정답 소리 재생
        pygame.init()
        pygame.mixer.init()
        soundplay = pygame.mixer.Sound('/Users/yoonseo/Desktop/python/python_basic/sound/good.wav')
        soundplay.play()
        cor_cnt += 1
    else:
        print("Wrong!")
        # 오답 소리 재생
        pygame.init()
        pygame.mixer.init()
        soundplay = pygame.mixer.Sound('/Users/yoonseo/Desktop/python/python_basic/sound/bad.wav')
        soundplay.play()

    n += 1      # 다음 문제 전환
    print()

end = time.time()   # End time
et = end - start    # 총 시간
et = format(et, ".3f")      # 소수 셋째자리 출력

if cor_cnt >= 3:
    print("합격")
else:
    print("불합격")

# 기록 DB 삽입
cursor.execute("INSERT INTO records('cor_cnt', 'record', 'regdate') VALUES (?, ?, ?)", (cor_cnt, et, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

# 수행 시간 출력
print("게임 시간 : ", et, "초", "\n정답 개수 : {}".format(cor_cnt))

# 시작 지점 코드
if __name__ == '__main__':
    pass