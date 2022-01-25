#병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램안에서 여러일을 쉽게 해결할 때 쓰임
#                   = Thread는 하나지만 마치 여러가지 일을 동시에 하는 것처럼 하기 때문에 효율성이 좋다
#제너레이터 실습
#Yield 실습
#Itertools 실습

#병렬성(Parallelism): 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도

# Generator Ex1

def generator_ex1():
    print('Start')
    yield 'A Point'
    print('Continue')
    yield 'B Point'
    print('End')

temp = iter(generator_ex1())

#print(temp)
#print(next(temp))
#print(next(temp))
#print(next(temp))

for v in generator_ex1():
    #print(v)
    pass

# Generator Ex2
temp2 = [x*3 for x in generator_ex1()]
temp3 = (x*3 for x in generator_ex1())

print(temp2)
print(temp3)

for i in temp3:
    print(i)

print()
print()

#Generator Ex3(중요 함수)
#filterfalse, accumulate, chain, product, groupby...

import itertools

#무한대 숫자 만들기
gen1 = itertools.count(1,2.5)

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
# ... 무한

# 조건

gen2 = itertools.takewhile(lambda n : n < 1000, itertools.count(1, 2.5))

for v in gen2:
    pass
    #print(v)

print()

# 필터 반대
gen3 = itertools.filterfalse(lambda n : n < 3, [1,2,3,4,5])

for v in gen3:
    print(v)

# 누적 합계
gen4 = itertools.accumulate([x for x in range(1,101)])

for v in gen4:
    print(v)

#연결1
gen5 = itertools.chain('ABCDE', range(1,11,2)) # 'ABCDE'와 1부터 11까지 2씩 증가되는 리스트를

print(list(gen5))


#연결2
gen6 = itertools.chain(enumerate('ABCDE'))

print(list(gen6))

#개별
gen7 = itertools.product('ABCDE')

print(list(gen7))

#연산(경우의수)
gen8 = itertools.product('ABCDE',repeat=2)

print(list(gen8))

#그룹화
gen9 = itertools.groupby('AAABBCCCCDDEEE')

#print(list(gen9))

for chr, group in gen9:
    print(chr, ' : ', list(group))
