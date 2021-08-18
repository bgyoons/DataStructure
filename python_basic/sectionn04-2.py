# section 04-2
# 문자열, 문자열 연산, 슬라이싱

str1 = "I am Boy."
str2 = "CoolBoy"
str3 = ""

print(len(str1), len(str2), len(str3)) # 글자수 세어줌

escape_str1 = "Do you have a \"coffee\""
print(escape_str1)
escape_str2 = "Tab\tTab\tTab"
print(escape_str2)


# Raw String
raw_s1 = r'C:\Document\Test\AAA'
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)

# 멀티라인
multi = \
"""
문자열

멀티라인

테스트
""" # 다음줄에 이어진다는 뜻
print(multi)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = 'def'
str_o4 = "Coolguy"

print(str_o1 * 10)
print(str_o2 + str_o3)
# print(str_o1 + 3) # ERROR 형이 다름
print('a' in str_o4) # 문자 'a'가 str_o4 포함 여부
print('a' not in str_o4) # 문자 'a'가 str_o4 미포함 여부

# 문자열 형 변환
print(str(77) + 'a') # 문자(string)로 뱐환되었기 떄문에  77와 'a'의 결합이 가능

# 문자열 함수
a = 'niceguy'
b = 'orange'

print(a.islower())
print(a.endswith('n'))
print(b.capitalize())
print(a.replace('nice', 'cool'))
print(list(reversed(b))) # list 해줘야함

print(a[0:3])
print(a[0:4])
print(a[0:len(a)])
print(a[:4])
print(a[:])
print(b[0:4:2])
print(b[1:-2])
print(b[::-1])