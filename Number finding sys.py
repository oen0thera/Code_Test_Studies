import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


def Solution(num):
  '''
  약수 찾기 시스템
  num= ~ 범위 이하의 약수
  '''
  i=0
  t=2
  appender=2
  number=1
  count=0
  result=[]
  while number<=num:
    if count==0:
      if t<=number**(0.5) and number%t==0:
        count+=1
        if number//t!=t:
            result.append(t)
            result.append(number//t)
        if number//t==t:
            result.append(t)
        print(t,number//t)
        t+=1
        count-=1
      if t<=number**(0.5) and number%t!=0:
        count+=1
        t+=1
        print(number)
        print(t)
        print(count)
        count-=1
      if t>number**(0.5):
        result.append(1)
        result.append(number)
        result.append('{}의 약수'.format(number))
        count+=1
        number+=1

        print(count)
        print(number)
        print('t:{}'.format(t))
        t=2
    count=0


  print(result)

Solution(87109)
