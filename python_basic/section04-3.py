# Section 04-3
# 리스트, 튜플

# 리스트 : 순서ㅇ, 중복ㅇ, 수정ㅇ, 삭제ㅇ
# 선언
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0] + d[1])
print(e[2][1])
print(e[-1][-2])

# 슬라이싱
print(d[0:3])
print(e[2][1:3])

# 연산
print(c + d)
print(c * 3)
print(str(c[0]) + 'hi')

# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000]
print(c)
c[1] = ['a', 'b', 'c']
print(c)

del c[1]
print(c)
del c[-1]
print(c)

print()

# 리스트 함수
y = [5, 2, 6, 3, 4]
print(y)
y.append(1) # 마지막에 추가
print(y)
y.sort() # 정렬
print(y)
y.reverse()
print(y)
y.insert(2, 7) # y[2] = 7 (인덱스 2번으로 삽입)
print(y)
y.remove(2) # 데이터 값 중에 숫자 2를 찾아 지금
print(y)
y.pop() # 맨 마지막을 없앰
print(y)

ex = [88, 77]
y.append(ex)
print(y)
y.extend(ex) # 리스트 자체를 삽입
print(y)

# 삭제 : del, remove, pop 

####################################

# 튜플 : 순서ㅇ, 중복ㅇ, 수정 X, 삭제 X
a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(c[3])
print(d[2][2])

print(d[2:])
print(d[2][0:2])

print(c + d)
print(c * 3)

# 튜플 함수
z = (5, 3, 2, 6, 7, 5)
print(z)
print(3 in z)
print(z.index(3)) # 인덱스 값을 반환
print(z.count(5))
