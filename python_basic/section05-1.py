# Section 05-1
# 파이썬 흐름제어(제어문)
# 조건문 실습

print(type(True))
print(type(False))

# EX1
if True:
    print("yes") # 단독 사용 가능

# EX2
if False:
    print("no") # 출력 안됨
    
# EX3
if False:
    print("no") # 출력 안됨
else:
    print("yes2")

# 관계연산자
# > , >=, <, <=, ==, !=

# 참 거짓 종류 (True, False)
# 참 : "내용", [내용], (내용), {내용}, 1, 내용이 있는 것
# 거짓 : "", [], (), {}, 0, 비어있는 것

city = "" # False

if city:
    print(">>>True")
else:
    print(">>>False")

# 논리 연산자
# and or not

a = 100
b = 60
c = 15

print('and : ', a > b and b > c)
print('or : ', a > b or b < c)
print('not : ', not a > b)
print(not False) # True
print(not True) # False

# 산술, 관계, 논리 연산자
# 우선순위 :  산술 > 관계 > 논리 순서로 적용
print(5 + 10 > 0 and not 7 + 3 == 10) # True and False >> False

score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print("합격")
else:
    print("불합격")

# 다중 조건문
num = 86

if num >= 90:
    print("num 등급 A", num)
elif num >= 80:
    print("num 등급 B", num)
elif num >= 70:
    print("num 등급 C", num)
else:
    print("XXXXXX")

# 중첩 조건문
age = 27
height = 175

if age >= 20:
    if height >= 170:
        print("A지망 지원 가능")
    elif height >= 160:
        print("B지망 지원 가능")
    else:
        print("지원 불가")
else:
    print("20세 이상 지원 가능")