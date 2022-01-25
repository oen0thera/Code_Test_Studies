#125874를 2배 하면 251748이 되는데, 이 둘은 같은 숫자로 이루어져 있고 순서만 다릅니다.

#2배, 3배, 4배, 5배, 6배의 결과도 같은 숫자로 이루어지는 가장 작은 수는 무엇입니까?

def Solution():
  Number=1
  import time
  start=time.time()
  while Number<1000000:
    List=sorted([i for i in str(Number)])
    List2=sorted([i for i in str(Number*2)])
    List3=sorted([i for i in str(Number*3)])
    List4=sorted([i for i in str(Number*4)])
    List5=sorted([i for i in str(Number*5)])
    List6=sorted([i for i in str(Number*6)])
    if List==List2==List3==List4==List5==List6:
      print('Result:{}'.format(Number))
      print('총실행시간:{}'.format(time.time()-start))
      break
    Number+=1

Solution()
