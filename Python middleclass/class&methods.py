
#list
car_company_list =['Ferrari','BMW','Audi']

#dictionary
#class
class Car():
    """
    Car Class
    """

#클래스 변수(모든 인스턴스가 공유)
    price_per_raise = 1.0

    def __init__(self,company,details):
        self._company = company
        self._details = details


    def __str__(self):
        return 'str : {} - {}'.format(self._company,self._details)

    def __repr__(self):
        return 'str : {} - {}'.format(self._company,self._details)

#Instacne Method
#Self:객체의 고유한 속성값을 사용

    def detail_info(self):
        print('Current ID: {}'.format(id(self)))
        print('Car Detail Info: {} {}'.format(self._company,self._details))

    def __del__(self):
        Car.car_count-=1
car1 = Car('Ferrari',{'color':'white'})
car2 = Car('BMW',{'color':'black'})
car3 = Car('Audi',{'color':'red'})

#ID확인
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)
print(car1 is car2)

#dir & __dict__ 확인
print(dir(car1))
print(car1.__dict__)

#Doctring
print(Car.__doc__)


#실행
car1.detail_info()
car2.detail_info()

#비교
print(car1.__class__,car2.__class__)
print(id(car1.__class__)==id(car2.__class__))

#에러
#Car.detail_info()
Car.detail_info(car2)

print(car1.car_count)

#접근
print(car1.car_count)
print(Car.car_count)

del car2
#삭제확인
print(Car.car_count)

#인스턴스 네임스페이스에 없으면 상위에서 검색
#즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색후 -> 상위(클래스 변수, 부모클래스 변수))


#Instance Method
def get_price(self):
    return 'Before Car Price-> company:{}, price:{}'.
