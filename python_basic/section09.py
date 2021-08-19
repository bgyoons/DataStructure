# Section 09
# 파일 읽기, 쓰기
# 읽기 모드 : r, 쓰기 모드(기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a
# .. : 상대 경로, . : 절대 경로

##### 파일 읽기 #####
# ex 01
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
print(dir(f))
f.close() # 반드시 close 리소스 반환

# ex 02
with open('./resource/review.txt', 'r') as f:
    # 자동 리소스 반환
    c = f.read()
    print(c)
    print(iter(c))

# ex 03
with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip()) # 양쪽 공백, 줄바꿈 제거

# ex 04
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read()   # 내용 없음
    print(">", content) 

# ex 05
with open('./resource/review.txt', 'r') as f:
    line = f.readline()   # 한 문장 단위로 읽음
    # print(line)
    while line:
        print(line, end="###")
        line = f.readline()  

# ex 06
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()   # 마지막에 escape 문자를 포함한 리스트 형태
    print(contents)
    for c in contents:
        print(c, end=" *** ")

# ex 07
score = []

with open('./resource/score.txt', 'r') as f:
    for line in f:
        score.append(int(line))   # 무조건 문자취급이라 변형해줘야함
    print(score)

print('Average : {:6.3f}'.format(sum(score)/len(score)))


##### 파일 쓰기 #####
# ex 01
with open('./resource/test1.txt', 'w') as f:
    f.write('niceman!\n')

# ex 02
with open('./resource/test1.txt', 'a') as f:
    f.write('goodman!!\n')

# ex 03
from random import randint # random int

with open('./resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 50)))
        f.write('\n')

# ex 04
with open('./resource/test2.txt', 'w') as f:
    list = ['Kim\n', 'Park\n', 'Cho\n']
    f.writelines(list)   # 리스트 -> 파일로 저장

# ex 05
with open('./resource/test3.txt', 'w') as f:
    print('Test Contents1!', file=f)
    print('Test Contents2!', file=f)