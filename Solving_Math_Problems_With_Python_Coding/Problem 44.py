#오각수는 Pn = n (3n − 1)/2 라는 공식으로 구할 수 있고, 처음 10개의 오각수는 다음과 같습니다.

#1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

#위에서 P4 + P7 = 22 + 70 = 92 = P8이 됨을 볼 수 있습니다. 하지만 두 값의 차인 70 − 22 = 48 은 오각수가 아닙니다.

#합과 차 모두 오각수인 두 오각수 Pj, Pk 에 대해서, 그 차이 D = | Pk − Pj | 는 가장 작을 때 얼마입니까?


import math
def Check(n):
  n=abs(n)
  p=(math.sqrt(n*24+1)+1)/6
  return p==int(p)

Fivestar=[]
for i in range(1,10000):
  Fivestar.append(i*(3*i-1)/2)

for i in Fivestar:
  for j in Fivestar:
    if i>j:
      if Check(i+j) and Check(i-j):
        print(i,j,i-j)

#못푼문제
#일일히 순회하는것이 오래걸릴 경우 따로 함수를 만들어 해당되는 부분만 체크하게 하자!
