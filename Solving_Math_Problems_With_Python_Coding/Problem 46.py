#크리스티안 골드바흐는 모든 홀수인 합성수를 (소수 + 2×제곱수)로 나타낼 수 있다고 주장했습니다.

#9 = 7 + 2×1^2
#15 = 7 + 2×2^2
#21 = 3 + 2×3^2
#25 = 7 + 2×3^2
#27 = 19 + 2×2^2
#33 = 31 + 2×1^2

#그러나 이 추측은 잘못되었음이 밝혀졌습니다.

#위와 같은 방법으로 나타낼 수 없는 가장 작은 홀수 합성수는 얼마입니까?

Usage=[i for i in range(1,100)]
Notprime=[i for i in range(1,10000) for j in range(1,i) if i%j==0 and j!=i and j!=1]
New=set(Notprime)
PrimeNum=[i for i in range(1,10000) if i not in New]
Notprime_and_odd=[i for i in New if i%2!=0]
Total_break=False
count=0
for i in Notprime_and_odd:
  count=0
  for j in Usage:
    if i-(j**2)*2>0:
      print(i-(j**2)*2,i,j)
      if i-(j**2)*2 in PrimeNum:
        count+=1
    if i-(j**2)*2<=0:
      if count==0 and i!=1:
        Result=i
        print(i-(j**2)*2,i,j)
        Total_break=True
      break
  if Total_break:
    break

print('Result:{}'.format(Result))
