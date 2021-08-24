# Section 05-1
# 파이썬 심화
# 객체 참조 중요한 특징들
# Python Object Referrance

print('EX-1 - ')
print(dir())

print()

# id vs __eq__(==) 증명
x = {'name': 'Kim', 'age': 33, 'city': "Seoul"}
y = x

print('EX2-1 - ', id(x), id(y))
print('EX2-2 - ', x == y)
print('EX2-3 - ', x is y)
print('EX2-4 - ', x, y)

x['class'] = 10
print('EX2-5 - ', x, y)     # 객체가 복사됨

z = {'name': 'Kim', 'age': 33, 'city': "Seoul", 'class': 10}
print('EX2-6 - ', x, z)  
print('EX2-7 - ', x is z)   # 같은 id값 => 같은 객체
print('EX2-8 - ', x is not z)
print('EX2-95 - ', x == z)   # 값이 같다

# 객체 생성 후 완전 불변 -> 즉, id는 객체 주소(정체성) 비교, ==(__eq__)는 값 비교

print()

# 튜플 불변형의 비교
tuple1 = (10, 15, [100, 1000])
tuple2 = (10, 15, [100, 1000])

print('EX3-1 - ', id(tuple1), id(tuple2))
print('EX3-2 - ', tuple1 is tuple2)
print('EX3-3 - ', tuple1 == tuple2)
print('EX3-4 - ', tuple1.__eq__(tuple2))

print()


# Copy, Deepcopy(깊은 복사, 얕은 복사)
# Copy
tl1 = [10, [100, 105], (5, 10, 15)]
tl2 = tl1
tl3 = list(tl1)

print('EX4-1 - ', tl1 == tl2)
print('EX4-2 - ', tl1 is tl2)
print('EX4-3 - ', tl1 == tl3)
print('EX4-4 - ', tl1 is tl3)

# 증명
tl1.append(1000)
tl1[1].remove(105)

print('EX4-5 - ', tl1)
print('EX4-6 - ', tl2)
print('EX4-7 - ', tl3)

print(id(tl1[2]))

tl1[1] += [110, 120]
tl1[2] += (110, 120)

print(id(tl1[2]))   # 주소값 바뀜

print('EX4-8 - ', tl1)
print('EX4-9 - ', tl2)   # 튜플 재할당(객체 새로 생성)
print('EX4-10 - ', tl3)

print()

# Deepcopy
# 장바구니
class Basket:
    def __init__(self, products=None):
        if products is None:
            self._products = []
        else:
            self._products = list(products)
    
    def put_prod(self, prod_name):
        self._products.append(prod_name)
    
    def del_prod(self, prod_name):
        self._products.remove(prod_name)

import copy

basket1 = Basket(['Apple', 'tv', 'snack', 'water', 'banana'])
basket2 = copy.copy(basket1)
basket3 = copy.deepcopy(basket1)

print('EX5-1 - ', id(basket1), id(basket2), id(basket3))
print('EX5-2 - ', id(basket1._products), id(basket2._products), id(basket3._products))   
# 일반 copy에서 객체의 주소는 다르지만 안에 있는 product는 같음, 표면적인 것만 복사
# deepcopy는 안에 존재하는 프로덕트 리스트형까지 알아서 복사를 해줌, 인스턴스 변수에 할당되어있는 아이디 주소까지 deepcopy를 함

basket1.put_prod('orange')
basket2.del_prod('snack')
print('EX5-3 - ', basket1._products)
print('EX5-4 - ', basket2._products)  
# orange가 같이 추가되고 snack는 같이 빠짐 -> 같은 객체 리스트를 참조하고 있기 때문
print('EX5-5 - ', basket3._products)

print()

# 함수 매개변수 전달 사용법
def mul(x, y):
    x += y
    return x

x = 10
y = 5
print('EX6-1 - ', mul(x, y), x, y)

a = [10, 100]
b = [5, 10]
print('EX6-2 - ', mul(a, b), a, b)  # 가변형 a -> 원본 데이터 변경

c = (10, 100)
d = (5, 10)
print('EX6-3 - ', mul(c, d), c, d)  # 불변형 c -> 원본 데이터 변경 안됨

print()

# 파이썬 불변형 예외
# str, bytes, frozenset, tuple : 사본 생성 X -> 참조 반환
# 어떻게 하든 하나의 id값으로 통일
tt1 = (1, 2, 3, 4, 5)
tt2 = tuple(tt1)
tt3 = tt1[:]

print('EX7-1 - ', tt1 is tt2, id(tt1), id(tt2))     # True
print('EX7-2 - ', tt1 is tt3, id(tt1), id(tt3))     # True

tt4 = (10, 20, 30, 40, 50)
tt5 = (10, 20, 30, 40, 50)
ss1 = 'Apple'
ss2 = 'Apple'

print('EX7-3 - ', tt4 is tt5, tt4 == tt5, id(tt4), id(tt5))
print('EX7-4 - ', ss1 is ss2, ss1 == ss2, id(ss1), id(ss2))