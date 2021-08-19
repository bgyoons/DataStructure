# Section 07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 선언
# class 클래스명:
#     함수

##### ex 01 #####
class UserInfo:
    # 속성, 매소드
    def __init__(self, name):
        self.name = name
    def user_info_p(self):
        print("Name : ", self.name)

# 네임스페이스
user1 = UserInfo("Kim")
print(user1.name)
user1.user_info_p()
user2 = UserInfo("Park")
print(user2.name)
user2.user_info_p()

print(id(user1))
print(id(user2))
print(user1.__dict__)
print(user2.__dict__)