#Chapter 04 - 01
#시퀀스형
#컨테이너(Container : 서로 다른 자료형[list, tuple, collections, deque])
# 플랫 ( Flat : 한개의 자료형 [str, bytes, bytearray, array.array, memoryview ])
#가변(list, bytearray, array.array, memoryview, deque)
#불변(tuple, str, bytes)
#리스트 및 튜플 고급

#지능형 리스트(Comprehending lists)
chars = '+_)(*&^%$#@!)'
code_list1 = []

for s in chars:
    #유니코드 리스트
    code_list1.append(ord(s))

print(code_list1)


# Comprehending lists
code_list2 = [ord(s) for s in chars]

print(code_list2)

#Comprehending lists + Map, Filter

code_list3 =[ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord,chars)))

print(code_list3)
print(code_list4)

print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

#Generator 생성

import array

#Generator: 한번에 한개의 항목을 생성(메모리 유지x)
tuple_g = (ord(s) for s in chars)
array_g = array.array('I',(ord(s) for s in chars))

print(type(tuple_g))
print(next(tuple_g))
print(array_g.tolist())
print()
print()

#제네레이터 예제
print(('%s' % c + str(n) for c in ['A' , 'B' , 'C' , 'D'] for n in range(1,21)))

for s in ('%s' % c + str(n) for c in ['A' , 'B' , 'C' , 'D'] for n in range(1,21)):
    print(s)

#리스트 주의
marks1 = [['~']* 3 for n in range(3)]
marks2 = [['~']*3]*3

marks1[0][1] = 'X'
marks2[0][1] = 'X'
print(marks1)
print(marks2)

# 증명
print([id(i) for i in marks1])
print([id(i) for i in marks2])
