'''
제곱근 2는 다음과 같은 연분수의 형태로 나타낼 수 있습니다.

2–√=1+12+12+12+…=1.414213…
위 식을 처음부터 한 단계씩 확장해 보면 아래와 같습니다.

1+12=32=1.5
1+12+12=75=1.4
1+12+12+12=1712=1.41666…
1+12+12+12+12=4129=1.41379…

그 다음은 9970, 239169, 577408 로 확장이 되다가, 여덟번째인 1393985 에 이르면 처음으로 분자의 자릿수가 분모의 자릿수를 넘어섭니다.

처음부터 1천번째 단계까지 확장하는 중에, 분자의 자릿수가 분모보다 많아지는 경우는 몇 번이나 됩니까?
'''
from fractions import Fraction
def Solution():
  Number=1+Fraction(1/2)
  count=0
  for i in range(1,1001):
    Number=1+Fraction(1/(1+Number))
    Numerator=[i for i in str(Number.numerator)]
    Denominator=[i for i in str(Number.denominator)]
    if len(Numerator)>len(Denominator):
      count+=1
  print(count)
Solution()
