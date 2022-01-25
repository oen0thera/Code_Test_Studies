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
  New_List=[]
  Final=[]
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
        sum=0
        for i in result:
            sum+=i
        New_List.append(sum)
        Final.append(New_List)
        result=[]
        New_List=[]
        count+=1
        number+=1

        print(count)
        print(number)
        print('t:{}'.format(t))
        t=2
    count=0
  print(result)
  print(Final)
  return Final



Result = Solution(10000)
print(Result)
Over_number=[]
for i in range(0,len(Result)):
    if i+1<Result[i][0]:
        Over_number.append(i+1)

print(Over_number)

Less_than_28123=[i for i in range(1,28124)]
print(Less_than_28123)
for a in Over_number:
    for b in Over_number:
        if a+b in Less_than_28123:
            Less_than_28123.remove(a+b)

print(Less_than_28123)
