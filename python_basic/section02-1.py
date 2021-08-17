# Section 02-1
# 파이썬 기초 코딩
# Print 구문의 이해

# 기본출력
print('hello world')
print("hello world")
print("""hello world""")

print()

# Separator 옵션 사용 (join)
print('T', 'E', 'S', 'T', sep='') # 작은 따옴표 사이에 문자값을 연결하여 붙여줌(공백)
print('2021', '08', '17', sep='-')
print('zerobase', 'gmail.com', sep='@')

# end 옵션 사용
print('welcome to', end=' ') # 끝 부분을 다음 문장과 연결해줌
print('the black parade', end=' ')
print('math notes')

print()

# format 사용 [], {}, ()
print('{} and {}'.format('You', 'Me'))
print('{0} and {1} and {0}'.format('You', 'Me')) # 숫자를 내부적으로 매핑(할당) You=0, Me=1
print("{a} are {b}".format(a='You', b='Me'))

print("%s's favorite number is %d" % ('bgn', 2)) # %s : 문자, %d : 정수, %f : 실수

print("Test1: %5d, Price: % 4.2f" % (776, 6534.132)) # 다섯자리 정수, 정수 네 자리 소숫점 두 자리 실수
print("Test1: {0: 5d}, Price: {1: 4.2f}".format(776, 5435.238)) # 딕셔너리
print("Test1: {a: 5d}, Price: {b: 4.2f}".format(a=776, b=5435.238))

# \escape 코드
print("'you'")
print('\'you\'')
print('\\you\\')