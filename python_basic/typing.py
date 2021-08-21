# Section 13 타이핑 게임 만들어보기

import random
import time
import sqlite3
import pygame
import datetime

words = []
n = 1
Ncorrect = 0

connDB = sqlite3.connect("python_basic/resource/typing.db", isolation_level=None)
cursor = connDB.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS typing(id INTEGER PRIMARY KEY AUTOINCREMENT, correct text, pass text, record text, regdate text)")

with open("python_basic/resource/word.txt", 'r') as f:
    for word in f:
        words.append(word.strip())
    # print(words)

input("\n* 영어단어 타자 연습하기 *")
input("\n준비되었으면 Enter 키를 눌러주세요.\n")

start = time.time()

while n <= 5:
    random.shuffle(words)
    q = random.choice(words)
    print("** Quiz #{}".format(n), "\n\n=>", q)

    x = input("=> ")

    if str(q) == str(x):
        pygame.init()
        pygame.mixer.init()
        Splay = pygame.mixer.Sound('python_basic/sound/good.wav')
        Splay.play()
        print("\n===Correct!!=== \n")
        Ncorrect += 1
    else:
        pygame.init()
        pygame.mixer.init()
        Splay = pygame.mixer.Sound('python_basic/sound/bad.wav')
        Splay.play()
        print("\n===Worng!!=== \n")

    n += 1

end = time.time()
Ntime = int(end) - int(start)

print("*******결과*******")
print("\n맞은 개수 : {}".format(Ncorrect), "개")
print("걸린 시간 : {}".format(Ntime), "초")

if Ncorrect >= 3:
    print("\n*******Congratulations!!!*******")
    Npass = "pass"
else:
    print("\nTry Again")
    Npass = "fail"

cursor.execute("INSERT INTO typing('correct', 'pass', 'record', 'regdate') VALUES (?, ?, ?, ?)", (Ncorrect, Npass, Ntime, datetime.datetime.now().strftime("%Y/%m/%d %H:%M%S")))