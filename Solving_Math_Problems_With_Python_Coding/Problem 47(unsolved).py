#서로 다른 두 개의 소인수를 갖는 수들이 처음으로 두 번 연달아 나오는 경우는 다음과 같습니다.

#14 = 2 × 7
#15 = 3 × 5

#서로 다른 세 개의 소인수를 갖는 수들이 처음으로 세 번 연속되는 경우는 다음과 같습니다.

#644 = 2² × 7 × 23
#645 = 3 × 5 × 43
#646 = 2 × 17 × 19

#서로 다른 네 개의 소인수를 갖는 수들이 처음으로 네 번 연속되는 경우를 찾으세요. 그 첫번째 수는 얼마입니까?
Notprime=[i for i in range(1,1000000) for j in range(1,int(i**(0.5)+1)) if i%j==0 and j!=i and j!=1]
New=set(Notprime)
global PrimeNum
PrimeNum=[i for i in range(1,1000000) if i not in New]
print(PrimeNum)

def Solution(num):
  Process=True
  result=[]
  while Process:
    for i in PrimeNum:
      if num%i==0 and num!=1 and i!=1:
        result.append(i)
        num=num//i
    if num==1:
      Result=set(result)
      return list(Result)
      Process=False
      break

def Final():
  initial=1
  Process=True
  sorting=[]
  while Process:
    print(initial)
    print(Solution(initial))
    if len(Solution(initial))!=4:
      initial+=1
    if len(Solution(initial))==4:
      if len(Solution(initial+1))==4:
        if len(Solution(initial+2))==4:
          if len(Solution(initial+3))==4:
            sorting=Solution(initial)+Solution(initial+1)+Solution(initial+2)+Solution(initial+3)
            print(sorting)
            for i in sorting:
              if sorting.count(i)>1:
                break
              if i==sorting[-1]:
                print(sorting)
                print(initial)
                return initial
      initial+=1

#43592
#[5449, 2, 4]

Final()
