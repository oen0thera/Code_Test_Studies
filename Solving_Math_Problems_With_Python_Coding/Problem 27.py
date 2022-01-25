#오일러는 다음과 같은 멋진 이차식을 제시했습니다.

#n2 + n + 41
#이 식의 n에다 0부터 39 사이의 수를 넣으면, 그 결과는 모두 소수가 됩니다.
#하지만 n = 40일 때의 값 402 + 40 + 41 은 40×(40 + 1) + 41 이므로 41로 나누어지고, n = 41일 때 역시 412 + 41 + 41 이므로 소수가 아닙니다.

#컴퓨터의 발전에 힘입어 n2 − 79n + 1601 이라는 엄청난 이차식이 발견되었는데, 이것은 n이 0에서 79 사이일 때 모두 80개의 소수를 만들어냅니다. 이 식의 계수의 곱은 -79 × 1601 = -126479가 됩니다.

#아래와 같은 모양의 이차식이 있다고 가정했을 때,

#n2 + an + b   (단 | a | < 1000, | b | < 1000)
#0부터 시작하는 연속된 n에 대해 가장 많은 소수를 만들어내는 이차식을 찾아서, 그 계수 a와 b의 곱을 구하세요.



def Solution(list):
  Alpha=[i for i in range(-1000,1001)]
  print(Alpha)
  Beta=[i for i in range(-1000,1001)]
  process=0
  count=0
  counting_a=0
  counting_b=0
  record=0
  number=[]
  calcul=0
  n=0
  while process==0:
    if process==0:
          a=Alpha[counting_a]
          b=Beta[counting_b]
          if calcul==0 and counting_a==2000:
            break
          if calcul==0 and counting_b<=2000:
            Package = ((n**2)+(n*a)+b)
            print( 'n^2 + {}n +{}'.format(a,b))
            if counting_b==2000:
              counting_b=0
              counting_a+=1
            if Package>0 and Package in list and calcul==0:
              n+=1
              count+=1

              if count>record and a!=0 and b!=0:
                record=count
                number.clear()
                number.append(a)
                number.append(b)
                print('현재 최고 기록: n^2 + {}n +{}'.format(number[0],number[1]))
                print('Highest number:{}'.format(number))
                print('Highest record:{}'.format(record))
                print(Package)
            elif Package not in list and calcul==0:
              calcul+=1
              counting_b+=1
              n=0
              count=0
              calcul-=1

  print('a:{},b:{}'.format(a,b))
  print('calcul:{}'.format(calcul))
  print('process:{}'.format(process))
  print()
  print('Highest number:{}'.format(number))
  print('Highest record:{}'.format(record))
  print(list)



n=3
setOfprimeNumbers=[2]

while len(setOfprimeNumbers)<10001:
    for i in setOfprimeNumbers:
        if n%i == 0:
            break
        if i==setOfprimeNumbers[-1]:
            setOfprimeNumbers.append(n)
    n+=1

print(setOfprimeNumbers)


Solution(setOfprimeNumbers)
