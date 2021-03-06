# Hash Table: 키(Key)에 데이터(Value)를 저장하는 데이터 구조
# 파이썬 딕셔너리(Dictionary) 타입이 해쉬 테이블의 예


### 간단한 해시 예 ###
# 해시 테이블 저장
hash_table = list([0 for i in range(10)])
print(hash_table)

# 초간단 해시함수
# 나머지 값을 사용하는 Division법
def hash_function(key):
    return key % 5  # return 값은 0 ~ 4 로 한정

# 해시 테이블에 저장
data1 = 'Andy'
data2 = 'zzndy'
data3 = 'Tqeff'
data4 = 'Anqeff'
print(ord(data1[0]), ord(data2[0]), ord(data3[0])) # 문자의 아스키코드 리턴
print(ord(data1[0]), ord(data1[0])%5)
print(ord(data1[0]), hash_function(ord(data1[0])))
    # 해시 테이블 단점
print(ord(data1[0]), ord(data4[0]))
    # 아스키 코드 값이 같아서 같은 곳에 저장이 됨(중복) : 충돌을 해결하기 위한 별도의 자료구조가 필요함

def storage_data(data, value):          
    key = ord(data[0])                  
    hash_address = hash_function(key)
    hash_table[hash_address] = value    # 슬롯

# 해시 테이블에서 특정 주소의 데이터를 가져오는 함수
storage_data('Andy', '01039849292')
storage_data('zzndy', '01039324352')
storage_data('Tqeff', '01020945292')

# 데이터 저장, 읽기
def get_data(data):
    key = ord(data[0])
    hash_address = hash_function(key)
    return hash_table[hash_address]

print(get_data('Andy'))


### 프로그래밍 연습 1 : 리스트 변수를 활용해서 해시 테이블 구현해보기
# 해시함수 : key % 8
# 해시 키 생성 : hash(data)
hashTable = list(0 for i in range(8))

# 키를 생성하는 함수 만들어야함!!!!!!
def getKey(data):
    return hash(data)

def hashFunction(key):
    return key % 8

def SaveData(data, value):
    # 키 값 생성    => 동시에 해버림..........
    # 해시함수 써서
    # hashAddress = hashFunction(key)
    hashAddress = hashFunction(getKey(data))
    # 밸류 할당
    hashTable[hashAddress] = value
    # return value  **아님

# 읽는 함수도 해주기..
def ReadData(data):
    hashAddress = hashFunction(getKey(data))
    return hashTable[hashAddress]

SaveData('a', '01029384858')
SaveData('b', '01098742468')
print(ReadData('a'))
print(hashTable)


### 충돌(Collision) 해결 알고리즘(좋은 해시 함수 사용하기)
# Chaining(Open Hashing) 기법
# 링크드 리스트로 데이터를 추가로 뒤에 연결시켜서 저장하는 기법
### 프로그래밍 연습 2 : 연습 1의 해시 테이블 코드에 Chaining 기법으로 충동해결 코드 추가
hashTable = list(0 for i in range(8))

def getKey(data):
    return hash(data)

def hashFunction(key):
    return key % 8

def SaveData(data, value):
    index_key = getKey(data)    # 해당 슬롯에 별도 저장
    hashAddress = hashFunction(index_key)
    if hashTable[hashAddress] != 0:
        for index in range(len(hashTable[hashAddress])):
            if hashTable[hashAddress][index][0] == index_key:
                hashTable[hashAddress][1] = value
                return
        hashTable[hashAddress].append([index_key.value])
    else:
        hashTable[hashAddress] = [[index_key, value]]

def ReadData(data):
    index_key = getKey(data) 
    hashAddress = hashFunction(index_key)
    if hashTable[hashAddress] != 0:
        for index in range(len(hashTable[hashAddress])):
            if hashTable[hashAddress][index][0] == index_key:
                return hashTable[hashAddress][index][1]
        return None    
    else:
        return None

# Linear Probing 기법
# hash address의 다음 address부터 맨 처음 나오는 빈 공간에 저장
### 프로그래밍 연습 3 : 연습 1의 해시 테이블 코드에 Linear Probing 기법으로 충동 해결 코드 추가
hashTable = list(0 for i in range(8))

def getKey(data):
    return hash(data)

def hashFunction(key):
    return key % 8

def SaveData(data, value):
    index_key = getKey(data)    # 해당 슬롯에 별도 저장
    hashAddress = hashFunction(index_key)
    if hashTable[hashAddress] != 0:
        for index in range(hashAddress, len(hashTable)):
            if hashTable[index] == 0:
                hashTable[index] = [index_key, value]
                return
            elif hashTable[index][0] == index_key:
                hashTable[index][1] = value
                return
    else:
        hashTable[hashAddress] = [index_key, value]

def ReadData(data):
    index_key = getKey(data) 
    hashAddress = hashFunction(index_key)
    if hashTable[hashAddress] != 0:
        for index in range(hashAddress, len(hashTable)):
            if hashTable[index][0] == 0:
                return None
            elif hashTable[index][0] == index_key:
                return hashTable[index][1]
    else:
        return None