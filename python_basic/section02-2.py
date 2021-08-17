# Section 02-2
# 파이썬 기초 코딩
# 몸풀기 코딩 실습

# import this
import sys

# 파이썬 기본 인코딩
print(sys.stdin.encoding) # 입력 : utf-8
print(sys.stdout.encoding) # 출력 : utf-8

# 출력문
print('My name is bgn.')

# 변수 선언
myName = 'Coolguy'

# 조건문
if myName == 'Coolguy':
    print('ok')

# 반복문
# 2 ~ 9구구단
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = '%(i,j),i*j)

# 한글로 선언도 가능하긴 하지만 권장 X

# 함수 선언
def greeting():
    print("hello!")

greeting()

# 클래스
class Cookie:
    pass

# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))