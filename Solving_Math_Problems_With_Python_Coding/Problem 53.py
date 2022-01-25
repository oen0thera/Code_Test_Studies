'''
1,2,3,4,5 다섯 숫자 중에서 세 개를 고르는 것에는 다음과 같은 10가지 경우가 있습니다.

123, 124, 125, 134, 135, 145, 234, 235, 245, 345

조합론에서는 이것을 5C3 = 10 또는 (53)=10 이라고 표기하며, 일반적인 식은 아래와 같습니다.

nCr =(nr)=
n!
r!(n−r)!
,   단 r ≤ n 이고, n! = n×(n−1)×...×3×2×1 이며 0! = 1.
이 값은 n = 23 에 이르러서야 23C10 =(2310)= 1144066 으로 처음 1백만을 넘게 됩니다.

1 ≤ n ≤ 100 일 때 nCr 값이 1백만을 넘는 경우는 모두 몇 번입니까? (단, 중복된 값은 각각 계산합니다)
'''
def factorial(n):
    if n==0:
        return 1
    if n>0:
        result=1
        for i in range(1,n+1):
            result=result*i
        return result
def Solution():
    from fractions import Fraction
    n=0
    count=0
    while n<=99:
      n+=1
      origin=[]
      for r in range(0,n+1):
        combin=Fraction(factorial(n)/(factorial(n-r)*factorial(r)))
        if combin>1000000:
          origin.append(combin)
      count+=len(list(origin))
    print('nCr값이 백만을 넘는 총 경우의 수 :{}'.format(count))

Solution()
