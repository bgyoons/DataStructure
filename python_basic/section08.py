# Section 08
# 파이썬 모듈과 패키지

# 예제
# 상대경로
# .. : 부모 디렉토리
# . : 현재 디렉토리

##### 사용 1(클래스) #####
from pkg.fibonacci import Fibonacci
# import *(All) : 불필요한 리소스 낭비, 필요한 것만 import

Fibonacci.fib(300)
print("ex2 : ", Fibonacci.fib2(400))
print("ex2 : ", Fibonacci().title)   # 인스턴스화

##### 사용 3(클래스) #####
from pkg.fibonacci import Fibonacci as fb

fb.fib(1000)

print("ex3 : ", fb.fib2(1600))
print("ex3 : ", fb().title)

##### 사용 4(함수) #####
import pkg.calculations as c

print("ex4 : ", c.add(10, 100))
print("ex4 : ", c.mul(10, 100))

##### 사용 5(함수) #####
from pkg.calculations import div as d

print("ex5 : ", int(d(100, 10)))

##### 사용 6(함수) #####
import pkg.prints as p
import builtins

p.prt1()
p.prt2()
print(dir(builtins))