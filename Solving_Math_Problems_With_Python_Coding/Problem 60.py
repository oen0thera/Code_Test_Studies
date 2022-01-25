'''
네 개의 소수 3, 7, 109, 673은 상당히 특이한 성질이 있습니다. 넷 중에 아무것이나 두 개를 골라서 어떤 쪽으로 이어붙이던지 그 결과도 소수가 됩니다. 예를 들어 7과 109를 고르면 7109와 1097 또한 소수입니다.
3, 7, 109, 673는 이런 성질을 가진 네 소수 중에서 그 합이 792로 가장 작습니다,

다섯 소수 중에 어떤 두 개를 골라 이어붙여도 소수가 되는 수들을 찾아서, 그 합의 최솟값을 구하세요.
'''
from itertools import *
def is_prime(n:int) -> bool:
  if n<2:
    return False
  if n in (2,3):
    return True
  if n%2 == 0 or n%3 == 0:
    return False
  if n<9:
    return True
  k,l = 5, n**0.5
  while k<=l:
    if n%k == 0 or n%(k+2) == 0:
      return False
    k+=6
  return True

PrimeNum=[i for i in range(1,1000) if is_prime(i)]
str_PrimeNum=[str(i) for i in PrimeNum]
Result=[]
Prime5=list(combinations([i for i in range(1,len(str_PrimeNum))],5))
print(PrimeNum)
