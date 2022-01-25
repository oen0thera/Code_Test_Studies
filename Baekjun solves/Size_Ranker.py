number = int(input())
ResultList=[]
for i in range(number):
  appender = list(map(int,input().split()))
  ResultList.append(appender)
Final=[]
for i in ResultList:
  count=0
  for j in ResultList:
    if i!=j:
      if i[0]<j[0] and i[1]<j[1]:
        count+=1

  Final.append(str(count+1))

print(' '.join(Final))
