Result=[]
for n in range(10, 1000000):
  op=0
  Number=[int(i) for i in str(n)]
  print(Number)
  for j in range(0,len(Number)//2):
    if Number[j]!=Number[len(Number)-(j+1)]:
      print(j,len(Number)-(j+1))
      op+=1
  if op>0:
    print('nope')
  if op==0:
    Result.append(n)

Final=[]
why=[]
for m in Result:
  count=0
  List=[i for i in bin(m)]
  List.remove(List[0])
  List.remove(List[0])
  print(List)
  for i in range(0,len(List)//2):
      if List[i]!=List[len(List)-(i+1)]:
        print(i,len(List)-(i+1))
        count+=1
  if count>0:
    print('nope')
  if count==0:
    Final.append(m)
    why.append(List)
print(Final)
print(sum(Final))
print(why)

#Another solution
total=0
for i in range(1,1000000):
    binary = str(bin(i))[2:]
    if i == int(str(i)[::-1]) and binary == binary[::-1]:
        total+=i
        print(i)
print(total)
