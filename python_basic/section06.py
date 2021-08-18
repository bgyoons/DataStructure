# Section 06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def 함수명(parameter):
#     code

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요

##### ex 01 #####
def hello(world):
    print("Hello", world)

hello("python")
hello(1234)

##### ex 02 - return #####
def helloReturn(world):
    val = "Hello " + str(world)
    return val

str = helloReturn("python!!!")
print(str)

##### ex 03 - 다중 리턴 #####
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = func_mul(100) # 리턴이 3개 이므로 받는 변수도 3개
print(val1, val2, val3)

##### ex 03 - 데이터 타입 반환 #####
def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3] # list, tuple, ...

lt = func_mul2(100)
print(lt, type(lt))

##### ex 04 #####
# *args, **kwargs : 가변인자
# * : tuple
# ** : dictionary
# 매개변수가 몇 개 넘어갈 지 모를 때, 
# 매개변수가 몇 개 넘어오느냐에 따라 함수의 작동을 달리 할 때
def args_func(*args):
    # print(args, type(args))

    # for t in args:
    #     print(t)

    # index 만들어줌
    for i, v in enumerate(args):
        print(i, v)

args_func('kim') # 튜플 형태로 작동
args_func('kim', 'park') 
args_func('kim', 'park', 'lee') 

# kwargs : 키워드 줄임말
def kwargs_func(**kwargs):
    # print(kwargs)

    for k, v in kwargs.items():
        print(k, v)

kwargs_func(name1 = 'Kim')
kwargs_func(name1 = 'Kim', name2 = 'Park', name3 = 'Lee')

##### ex 05 #####
# 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs):
# arg1, arg2 필수적으로 함수를 호출할 때 써야하는 변수
    print(arg1, arg2, args, kwargs)

example_mul(10, 20)
example_mul(10, 20, 'park', 'kim', age1=24, age2=20)

# 중첩함수(클로저)
def nested_func(num):
    def func_in_func(num):
        print('>>>', num)
    print("in func")
    func_in_func(num + 10000)

nested_func(10000)

##### ex 06 (hint) #####
# 함수의 입력값과 출력값을 알려줄 수 있음
def func_mul3(x : int) -> list: # x는 int지만 list로 반환(출력)됨
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3] 

print(func_mul3(5))

##### ex 07 - 람다식 예제 #####
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수 : 객체 생성 -> 리소스(메모리) 할당
# 람다 : 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당
def mul_10(num : int) -> int:
    return num * 10

var_func = mul_10 # 함수를 사용하지 않았지만 이미 메모리 할당이 되어있음
print(var_func)
print(type(var_func))

print(var_func(10))

# 람다 - lambda input(parameter) : output(return)
lambda_mul_10 = lambda num : num * 10

print('>>>', lambda_mul_10(10))

def func_final(x, y, func):
    print(x * y * func(10))

func_final(10, 10, lambda_mul_10)

print(func_final(10, 10, lambda x : x * 1000))