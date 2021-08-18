# Section 05-2
# 파이썬 흐름제어(반복문)
# 반복문 실습

# 코딩의 핵심 > 조건 해결 중요

# 기본 반복문 : for, while

v1 = 1
while v1 < 11:
    print("v1 is : ", v1)
    v1 +=1

for v2 in range(10):
    print("v2 is :", v2)

for v3 in range(1, 100):
    print("v3 is :", v3)

# 1 ~ 100 sum
sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print('1 + 2 + ... + 100 = ', sum1)
print('1 + 2 + ... + 100 = ', sum(range(1, 101)))
print('1 + 2 + ... + 100 = ', sum(range(1, 101, 2)))

# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 딕셔너리 : 반복 가능
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

names = ['Kim', 'Park', 'Cho', 'Choi', 'Yoo']

for v in names:
    print('You are : ', v)

word = "dreams" # immutable

for s in word:
    print('Word : ', s)

my_info = {
    "name" : "Kim",
    "age" : 25,
    "city" : "Seoul"
}

# 기본값은 키
for key in my_info:
    print("my_info", key)

# 값
for key in my_info.values():
    print("my_info", key)

# 키
for key in my_info.keys():
    print("my_info", key)

# 키 and 값
for k, v in my_info.items():
    print("my_info", k, v)

name = "KennRY"

for n in name:
    if n.isupper():
        print(n.lower()) # n이 한 글자씩 들어옴
    else:
        print(n.upper())


# break
# 내가 찾고자 하는 조건이 맞다면 반복문을 즉시 탈출
numbers = [14, 2, 3, 61, 7, 85, 24, 1, 86, 15]

for num in numbers:
    if num == 84:
        print('found : 84')
        break
    else:
        print('not found : ', num)

# for else 구문(for 반복문이 정상적으로 수행된 경우 else 블럭 수행)
for num in numbers:
    if num == 84:
        print('found : 84')
        break
    else:
        print('not found : ', num)
else:
    print('not found 84........') # break를 안 만나면 수행됨


# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        continue # 조건에 해당되는 값은 수행되지 않고 다음 순회할 값으로 이동
    print("타입 : ", type(v))


### 리스트 컴프리헨션 ###

# 일반적인 방법
numbers = []

for n in range(1, 101):
    numbers.append(n)
print(numbers)

# list comprehension
numbers2 = [x for x in range(1, 101)]

print(numbers)