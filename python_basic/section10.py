# Section 10
# 파이썬 에러처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임) 프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일, 문법 체크

# SyntaxError : 잘못된 문법
# print('test)
# if True
#     pass

# NameError : 참조변수 없음
a = 10
b = 15
# print(c)

# ZeroDivisionError : 0 나누기 에러
# print(10 / 0)

# IndexError : 인덱스 범위 오버
x = [10, 20, 30]
print(x[0])
# print(x[3])   # 예외 발생

# KeyError
dic = {'name': 'Kim', 'Age': 33, 'City': 'Seoul'}
# print(dic['hobby'])       # 없는 키 조회
print(dic.get('hobby'))   # None으로 리턴됨

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외
import time
print(time.time())
# print(time.month()) # 예외 발생

# ValueError : 참조 값이 없을 때 예외
x = [1, 5, 9]
# x.remove(10)
# x.index(10)

# FileNotFoundError
# f = open('test.txt', 'r') # 얘외 발생

# TypeError : 자료형에 맞지 않는 연산을 수행 할 경우
x = [1, 2]
y = (1, 2)
z = 'test'
# print(x + y) 
print(x + list(y))
# print(x + z)

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생시 예외 처리 코딩 권장 (EAFP 코딩 스타일)

# 예외 처리 기본
# try: 에러가 발생 할 가능성이 있는 코드 실행
# except: 에러명1
# except: 에러명2
# else: 에러가 발생하지 않았을 경우 실행
# finally: 항상 실행

# ex 01
name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim'    # Cho 예외 발생
    x = name.index(z)
    print('{} Found it! in name'.format(z, x + 1))
except ValueError:
    print('Not found it! - Occurred ValueError')
else:
    print('Ok! else!')   # try가 정상 작동했을 때 유기적으로 발생되는 것

# ex 02
name = ['Kim', 'Lee', 'Park']

try:
    z = 'Ki'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x + 1))
except:   # 무슨 에러가 발생할지 모를 때(모든 에러 캐치)
    print('Not found it! - Occurred Error')
else:
    print('Ok! else!')

# ex 03
name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x + 1))
except:   # 무슨 에러가 발생할지 모를 때(모든 에러 캐치)
    print('Not found it! - Occurred Error')
else:
    print('Ok! else!')
finally:
    print("finally Ok!")

# ex 04
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴
try:
    print('try')
finally:
    print('finally')

# ex 05
name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x + 1))
except ValueError as l:   
    print(l)
    print('Not found it! - Occurred ValueError')
except IndexError:   
    print('Not found it! - Occurred IndexError')
except Exception: 
# except 중에 처음으로 등장하면 에러를 전부 잡으므로 안됨(순서 중요)
    print('Not found it! - Occurred Error')
else:
    print('Ok! else!')
finally:
    print("finally Ok!")
    print('Ok, finally!')

# ex 06
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생
try:
    a = 'Kim'
    if a == 'Kim':
        print('ok!')
    else:
        raise ValueError
except ValueError:
    print('Error occurred!!')
except Exception as f:
    print(f)
else:
    print('ok!!!!!!!!!!!!!')