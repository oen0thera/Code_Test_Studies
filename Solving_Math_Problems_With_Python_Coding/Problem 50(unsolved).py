import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#41은 소수이면서 다음과 같은 6개의 연속된 소수의 합으로도 나타낼 수 있습니다.

#41 = 2 + 3 + 5 + 7 + 11 + 13
#이것은 100 이하에서는 가장 길게 연속된 소수의 합으로 이루어진 소수입니다.

#1000 이하에서는 953이 연속된 소수 21개의 합으로 가장 깁니다.

#1백만 이하에서는 어떤 소수가 가장 길게 연속되는 소수의 합으로 표현될 수 있습니까?

def Solution():
    Notprime=[i for i in range(2,1000000) for j in range(1,int(i**(0.5)+1)) if i%j==0 and j!=i and j!=1]
    New=set(Notprime)
    PrimeNum=[i for i in range(2,1000000) if i not in New]
    record=0
    resume=0
    prev=0
    for i in range(0,len(PrimeNum)):
      if i>0:
        if utter>len(PrimeNum[i:]):
          break
      for j in range(i,len(PrimeNum)):
        if i<j:
          print(i,j,record,resume)
          if sum(PrimeNum[i:j]) in PrimeNum and record<len(PrimeNum[i:j]):
            record=len(PrimeNum[i:j])
            resume=sum(PrimeNum[i:j])
            utter=j-i
            print(sum(PrimeNum[i:j]))
          if sum(PrimeNum[i:j]) in PrimeNum and record>len(PrimeNum[i:j]):
            break
    print(record)
    print(resume)

#어거지로 푼 풀이,,, 이 코딩은 답이 딱 나오지도 않고, 시간도 오래걸림...

N=1000000
prime=[2]

for n in range(3,N):
    k=0
    while prime[k]<n**0.5:
        if n%prime[k]==0 or k>=len(prime)-1:
            break
        else: k+=1
    if prime[k]>n**0.5:
        prime.append(n)     #N보다 작은 소수 목록을 만들었음.

ma=0

for i in range(0,len(prime)):
	sum=0
	for j in range(0,len(prime)-i):
		sum=sum+prime[i+j]   #i번째부터 j번째까지의 소수를 더해라
		if sum>N:
			break
		if sum in prime and ma<j+1:
			ma=j+1
			tu=(ma,sum,i+1)
			print(f"{tu[2]}번째 소수인 {prime[tu[2]-1]}부터 {tu[0]}개의 소수를 더하면 {tu[1]}")
