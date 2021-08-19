# Section 07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

##### ex 01 #####
# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 매소드 사용 가능

# 라면 -> 속성(종류, 회사, 맛, 면 종류, 이름) : 부모

class Car:
    """Parent Class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car Class "Show Method!"'

class BmwCar(Car):
    """Sub Class"""
    def __init__(self, tp, color, car_name):
        super().__init__(tp, color)   # 부모의 init 매소드 호출
        self.car_name = car_name

    def show_model(self) -> None: # hint
        return "Your car name : %s" % self.car_name

class BenzCar(Car):
    """Sub Class"""
    def __init__(self, tp, color, car_name):
        super().__init__(tp, color) 
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your car name : %s" % self.car_name

    def show(self):
        print(super().show())  # 부모 것도 호출
        return "Car Info : %s %s %s" % (self.car_name, self.type, self.color)

# 일반 사용
model1 = BmwCar('sedan', 'red', '520d')

print(model1.color) # Super
print(model1.type) # Super
print(model1.car_name) # Sub
print(model1.show()) # Super
print(model1.show_model()) # Sub
print(model1.__dict__)

# Method Overriding(오버라이딩)
model2 = BenzCar('suv', 'black', '220d')
print(model2.show()) # Sub

# Parent Method Call
model3 = BenzCar('sedan', 'sliver', "350s")
print(model3.show())

# Inheritance Info
print(BmwCar.mro()) # 상속 관계가 나타남
print(BenzCar.mro())

###### ex 02 #####
# 다중 상속

class X():
    pass

class Y():
    pass

class Z():
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z):
    pass

print(M.mro())
print(A.mro())