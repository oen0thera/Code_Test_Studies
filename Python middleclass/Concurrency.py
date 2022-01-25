#병행성(Concurrency)

#병행성, 흐름제어 설명
#이터레이터(Iterator)
#제너레이터(Generator)
#_iter_, _next_
#클래스 기반 제너레이터 구현

# 파이썬 반복 가능한 타입
# collections, text file, list, Dict, Set, Tuple, unpacking, *args : iterable

# 반복 가능한 이유? -> iter(x) 함수 호출
t = 'ABCDEFGHIJKLMNOPQRSTUWXYZ'

for c in t:
    #print(c)
    pass

# while
w = iter(t)

while True:
    try:
        print(next(w))
    except StopIteration:
        break

print()

# 반복형 확인

from collections import abc

print(dir(t))
print(hasattr(t,'__iter__')) #hasattr: 이 특성을 가지고 있니?...
print(isinstance(t, abc.Iterable))

print()
print()


# next 패턴
class WordSplitter:
    def __init__(self,text):
        self._idx =0
        self._text = text.split(' ')

    def __next__(self):
        print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration. ^_^')
        self._idx +=1
        return word

    def __repr__(self):
        return 'WordSplit(%s))' % (self._text)

wi = WordSplitter('Do today what you could do tomorrow')
print(wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
#print(next(wi))

print()
print()

# Generator
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가 증가 후 메모리 사용량 증가 -> 제네레이터 사용 권장
# 2. 단위 실행 가능한 코루틴(Coroutine) 구현과 연동
# 3. 작은 메모리 조각 사용

class WordSplitGenerator:
    def __init__(self,text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word #제네레이터 ( important!)
                        #index를 굳이 사용하지 않아도 위치정보, 다음에 반환할 값에 대한상태, 레퍼런스들을 기억

        return
    def __repr__(self):
        return 'WordSplitGenerator(%s))' % (self._text)

wg = WordSplitGenerator('Do today what you could do tomorrow')

wt = iter(wg)
print(wt
, wg)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))

print()
print()
