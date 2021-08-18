# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
from functools import partial


q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

if q1["가을"]:
    print(q1["가을"])

for k in q1.keys():
    if k == "가을":
        print(q1[k])

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

if q1["가을"] == "사과":
    print("O")
else:
    print("X")

for k, v in q2.items():
    if v == "사과":
        print(k, v)
        break
else:
    print("사과 없음")

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
score = 39

if score > 80:
    print("A")
elif score > 60:
    print("B")
elif score > 40:
    print("C")
elif score > 20:
    print("D")
else:
    print("E")

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
a = 12
b = 6
c = 18

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
elif b > c:
    if b > a:
        print(b)
    else:
        print(a)
elif c > a:
    if c > b:
        print(c)
    else:
        print(b)
else:
    print("모순")

best = a

if b > a:
    best = b

if c > b:
    best = c

print('best : ', best)

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
jumin = "939494-3929393"

# if int(jumin[7]) % 2 == 0:
if int(jumin[7]) == 2 or int(jumin[7]) == 4:
    print("female")
else:
    print("male")

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]

for trd in q3:
    if trd == "정":
        continue
    else:
        print(trd)

# 리스트 컴프리헨션
trd = [x for x in q3 if x != "정"]
print(trd)

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
for n in range(1, 101):
    if n % 2 == 1:
        print(n, end=" ")
        
print()

# 리스트 컴프리헨션
sth = [n for n in range(1, 101) if n % 2 == 1]
print(sth)

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

for fth in q4:
    if len(fth) >= 5:
        print(fth)

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for fvth in q5:
    if fvth.islower():
        print(fvth)

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for sxth in q6:
    if sxth.islower():
        print(sxth.upper())
    else:
        print(sxth.lower())