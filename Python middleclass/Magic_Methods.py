#Special Method(Magic Method)
#파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)
#클래스안에 정의할 수 있는 특별한(Built-in) 메소드

#기본형
print(int)
print(float)

#모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))

n = 10

print(type(n))
print(n.__add__(100))
print(n.__doc__)
print(n.__bool__(),bool(n))
print(n*100,n.__mul__(100))

#클래스 예제
class Fruit:
    def __init__(self,name,price):
        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit Class Info:{},{}'.format(self._name,self._price)

    def __add__(self,x):
        return self._price + x._price

    def __sub__(self,x):
        return self._price - x._price

    def __le__(self,x):
        if self._price <= x._price:
            return True
        else:
            return False

    def __ge__(self,x):
        if self._price >= x._price:
            return True
        else:
            return False


#인스턴스 생성
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

print(s1+s2)
print(s1-s2)
print(s1>=s2)
print(s1<=s2)

#클래스 예제2
#(5,2)

class Vector(object):

    def __init__(self,*args):
        '''
        Create a vector, example: v = Vector(5,10)
        '''
        if len(args)==0:
            self._x,self._y = 0,0
        else:
            self._x,self._y = args

    def __repr__(self):
        '''Return the vector information '''
        return 'Vector(%r,%r)'%(self._x,self._y)

    def __add__(self,other):
        '''Return the vector addition of self and other'''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self,other):
        return Vector(self._x * other, self._y * other)

    def __bool__(self):
        return bool(max(self._x,self._y))
print(Vector.__init__.__doc__)

#Vector 인스턴스 생성
v1 = Vector(5,7)
v2 = Vector(23,35)
v3 = Vector()

#매직 메소드 출력
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)
print(v1,v2,v3)
print(v1+v2)
print(v1*3)
print(bool(v1),bool(v2))
print(bool(v3))
