#소수 중에서 각 자리의 숫자들을 순환시켜도 여전히 소수인 것을 원형 소수(circular prime)라고 합니다. 예를 들어 197은 971, 719가 모두 소수이므로 여기에 해당합니다.

#이런 소수는 100 미만에 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97 처럼 13개가 있습니다.

#그러면 1,000,000 미만에는 모두 몇 개나 있을까요?

#Solution 2
n=3
next=0
count=0
setOfprimeNumbers=[2]
mind=0
Result=[]
while setOfprimeNumbers[-1]<1000001:
    for i in setOfprimeNumbers:
        if n%i == 0:
            break
        if i==setOfprimeNumbers[-1]:
            setOfprimeNumbers.append(n)
            print(setOfprimeNumbers[-1])
    n+=1
print(setOfprimeNumbers)

while mind==0:
    for m in setOfprimeNumbers:
      print(m)
      New=[int(i) for i in str(m)]
      Flyer=[]
      for i in range(0,len(New)):
        New.append(New[0])
        New.remove(New[0])
        Lon=New[:]
        List=[str(i) for i in Lon]
        Flyer.append(int(''.join(List)))
      for j in Flyer:
          if j not in setOfprimeNumbers:
            count+=1
      if count==0:
        Result.append(m)
      count=0
      if m==setOfprimeNumbers[-1]:
        mind+=1
        break
print(Result)
print(len(Result))
