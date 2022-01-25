#두 자리 수 *3의 첫번째 자리를 여러가지로 바꿨을 때 가능한 아홉 가지의 결과 중에서 13, 23, 43, 53, 73, 83의 여섯 개는 소수입니다.

#56**3 의 3번째와 4번째 자리를 동일한 숫자로 바꿔서 만들어지는 10개의 다섯자리 수 중에서는 아래에서 보듯이 7개가 소수가 되며, 이것은 이런 식으로 7개의 소수가 만들어지는 첫번째 경우입니다. 이 소수 집단의 첫번째 수인 56003은 이런 성질을 갖는 가장 작은 소수입니다.

#56003, 56113, 56333, 56443, 56663, 56773, 56993
#위의 예처럼 원래의 일부를 동일한 숫자로 치환했을 때 8개의 소수 집단이 만들어지는 경우를 찾고, 그 집단에 속한 가장 작은 소수를 구하세요.
#치환하는 자리는 인접하지 않아도 되고, 가장 앞부분을 치환하는 경우 거기에 0은 올 수 없습니다.

def Solution():
  from itertools import combinations
  from copy import copy
  Notprime=[i for i in range(100000,1000000) for j in range(1,int(i**(0.5)+1)) if i%j==0 and j!=i and j!=1]
  New=set(Notprime)
  PrimeNum=[i for i in range(100000,1000000) if i not in New]
  print(PrimeNum)
  Total_Break=False
  for i in PrimeNum:
    if i>100000:
      if Total_Break==False:
        Counting_pos=[j for j in str(i)]

        counts=len(Counting_pos)
        Range=[j for j in range(0,counts)]
        Result=[]
        for k in range(0,counts+1):
          comb=list(map(set,combinations(Range,k)))
          if k:
            Result.append(comb)
        for u in Result:
          for e in range(0,len(u)):
            Tide=[]
            if 0 not in u[e]:
              for p in range(0,10):
                New=copy(Counting_pos)

                for n in u[e]:
                  del New[n]
                  New.insert(n,str(p))
                Number=int(''.join(New))
                if Number in PrimeNum and Number!=i:
                  Tide.append(Number)
                print(i)
                if len(Tide)==8:
                  print(Tide)
                  Total_Break=True
            if 0 in u[e]:
              for p in range(1,10):
                New=copy(Counting_pos)

                for n in u[e]:
                  del New[n]
                  New.insert(n,str(p))
                Number=int(''.join(New))
                if Number in PrimeNum and Number!=i:
                  Tide.append(Number)
                print(i)
                if len(Tide)==8:
                  print(Tide)
                  Total_Break=True
      if Total_Break==True:
          print('Result:{}'.format(i,Tide))
          raise IndexError



Solution()
