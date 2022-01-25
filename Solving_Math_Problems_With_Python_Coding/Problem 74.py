'''
145는 각 자릿수의 계승(팩토리얼) 값을 모두 더했을 때 자기 자신이 되는 수로 잘 알려져 있습니다.

1! + 4! + 5! = 1 + 24 + 120 = 145

그보다 덜 유명하긴 하지만 169는 위와 같은 방법으로 계산해서 자기 자신으로 되돌아오는 데 가장 많은 단계를 거치는 수로, 그런 특성을 가진 수는 3개밖에 없다고 합니다.

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

어떤 수로 시작해도 결국 위와 같은 반복 루프에 들어간다는 사실은 어렵지 않게 증명이 가능한데, 몇 개 수의 예를 들면 다음과 같습니다.

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

69로 시작하면, 반복이 일어나기 전에 다섯 번의 단계를 거친 다음에 루프에 들어갑니다. 1백만 이하의 수로 시작하는 경우는 최대 60번의 반복되지 않는 단계가 존재합니다.

1백만 이하의 수로 시작했을 때, 반복되지 않는 단계를 정확히 60번 거치는 경우는 모두 몇 번이나 됩니까?
'''

def factorial(number:int, currentNumber:int, result:int):
  currentNumber-=1
  if number>1 and currentNumber>1:
    result=result*currentNumber
    result = factorial(number, currentNumber, result)
  if number==0:
    return 1

  if result!=None:
    return result

def positionSquare(number:int,List:list):
  strNum = str(number)
  splitNum = [int(i) for i in strNum]
  result=0
  for i in splitNum:
    fact = i
    fact = factorial(i,i,fact)
    result+=fact
  if result not in List:
    List.append(result)
    positionSquare(result,List)
  else:
    return List

count=0
for i in range(1,1000000):
  number=i
  List=[number]
  positionSquare(number,List)
  if len(List)==60:
    count+=1

print('count:',count)
