#수 145는 신기한 성질이 있습니다. 각 자릿수의 팩토리얼(계승)을 더하면  1! + 4! + 5! = 1 + 24 + 120 = 145 처럼 자기 자신이 됩니다.

#이렇게 각 자릿수의 팩토리얼을 더하면 자기 자신이 되는 모든 수의 합을 구하세요.

#단, 1! = 1 과 2! = 2 의 경우는 덧셈이 아니므로 제외합니다.

def Solution(n):
  Result=[]
  count=3
  result=1
  Final=0
  a=1
  while count<n:
    List=[int(i) for i in str(count)]
    for i in List:
      if i>0:
        for j in range(1,i+1):
          result=result*j
        Final+=result
        result=1
      if i==0:
        Final+=1
    print(count, Final)
    if Final==count:
      Result.append(count)
    Final=0
    count+=1
  print(Result)
  print(sum(Result))
Solution(45000)
