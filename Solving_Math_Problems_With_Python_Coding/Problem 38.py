#수 192에 1, 2, 3을 각각 곱합니다.

#192 × 1 = 192
#192 × 2 = 384
#192 × 3 = 576
#곱한 결과를 모두 이어보면 192384576 이고, 이것은 1 ~ 9 팬디지털(pandigital) 수입니다. 이런 과정을 편의상 '곱해서 이어붙이기'라고 부르기로 합니다.

#같은 식으로 9와 (1, 2, 3, 4, 5)를 곱해서 이어붙이면 918273645 라는 1 ~ 9 팬디지털 수를 얻습니다.

#어떤 정수와 (1, 2, ... , n)을 곱해서 이어붙였을 때 얻을 수 있는 가장 큰 아홉자리의 1 ~ 9 팬디지털 수는 무엇입니까? (단 n > 1)

#Condition: 수는 1~n까지 순회하면서 곱할것
#           곱한 결과물이 9자리를 넘어서면 break
#           수의 범위는 정해지진 않았음

def Solution(n):
  count=2
  List=[]
  Result=[]
  compare=['1','2','3','4','5','6','7','8','9']
  while count<n:
    for i in range(1,10):
      List+=[ j for j in str(count*i)]
      print(List)
      if len(List)>9:
        List=[]
        count+=1
        break
      if len(List)==9:
        New = sorted(List)
        if New==compare:
          Result.append(int(''.join(List)))
        List=[]
        New=[]
        count+=1
        break
  print(max(sorted(Result)))

Solution(100000)

#100만까지 해도 값은 동일함
