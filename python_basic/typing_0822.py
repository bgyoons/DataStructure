# Section 13 타이핑 게임 만들어보기
# 타이핑 게임
# 0822

import random
import time
import sqlite3
import datetime
# import pygame

# DB 생성 / Cursor
conn = sqlite3.connect('python_basic/resource/typing0822.db', isolation_level=None)

cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS typing0822(id INTEGER PRIMARY KEY AUTOINCREMENT, correct INTEGER, grade text, record INTEGER, regdate text)")

# 변수 선언
words = []      # 출제 단어
n = 1           # 게임 횟수 및 문제 번호
correctN = 0    # 맞은 개수
grade = ""      # 등급

# 출제 단어 불러오기 & 출제 단어 리스트에 삽입
with open('python_basic/resource/word.txt', 'r') as f:
    for w in f:
        words.append(w.strip())
    # print(words)

input("R U Ready?\n")
input("Press Enter Key\n")

start = time.time()

while n <= 5:
    random.shuffle(words)
    w = random.choice(words)
    
    print('** Quiz #{}'.format(n), '\n')
    print('=> {}'.format(w))
    x = input('=> ')

    if w == x:
        print('\nCorrect\n')
        correctN += 1
    else:
        print('\nWrong\n')
    n += 1

end = time.time()
record = int(end) - int(start)

print('====================')

if correctN >= 3:
    print("\n합격입니다.")
    if correctN == 5:
        grade = "A"
    else:
        grade = "B"
else:
    print("\n불합격입니다.")
    if correctN == 2:
        grade = "C"
    else:
        grade = "F"

cursor.execute("INSERT INTO typing0822('correct', 'grade', 'record', 'regdate') VALUES (?, ?, ?, ?)", (correctN, grade, record, datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')))

print('\n맞은 개수 : {}'.format(correctN), '개')
print('등급 : {}'.format(grade))
print('걸린 시간 : {}'.format(record), '초')

if __name__ == '__main__':
    pass