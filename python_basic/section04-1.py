# 데이터 타입

v_str1 = 'Coolguy'
v_bool = True
v_str2 = "goodguy"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "bgn",
    "age" : 25
}
v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {7, 8, 9}

print(type(v_dict))

a = 5.
b = 4
result = a + b
print(result, type(result))

# 형변환
# int, float, complex
print(int(result))
print(int(True))
print(int('3'))

# 수치 연산 함수
print(abs(-7)) # 절댓값
n, m = divmod(100, 8) # n이 몫, m이 나머지
print(n, m)

import math

print(math.ceil(5.1)) # 올림
print(math.floor(3.8)) # 내림