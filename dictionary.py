class Dog:
    species= 'firstdog'

    def __init__(self,name,age):
        self.name = name
        self.age = age


class SelfText:
    def func1(self):
        print('Func1 called')
    def func2(self):
        print('Func2 called')


class Warehouse:
    stock_num = 0

    def __init__(self,name):
        self.name = name
        Warehouse.stock_num+=1

    def __del__(self):
        Warehouse.stock_num-=1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)

print(user2.name)
print(user1.name)
print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__)
