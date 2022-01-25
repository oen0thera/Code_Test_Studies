#1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.
#그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?

def Solution(range):
  count=1
  tide=0
  i=1
  num=1
  while count<=range:
    if i<=range:
      if num%i==0:
        print(i)
        count+=1
        i+=1
        print('pass')
      else:
        if i%2==0:
          num=num*2
          count=1
          tide+=1
          i=1
        elif i%3==0:
          num=num*3
          count=1
          tide+=1
          i=1
        elif (i%5)%5==0:
          num=num*5
          tide+=1
          count=1
          i=1
        elif (i%7)%7==0:
          num=num*7
          tide+=1
          count=1
          i=1
        else:
          num=num*i
          tide+=1
          count=1
          i=1
        print('reset')
        print(tide)
        tide=0
    if count==range+1:
      print(num)
      break
    if tide==500:
        print(num)


Solution(50)
