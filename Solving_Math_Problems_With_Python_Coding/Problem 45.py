#삼각수, 오각수, 육각수는 아래 식으로 구할 수 있습니다.

#삼각수	 	Tn = n (n + 1) / 2	 	1, 3, 6, 10, 15, ...
#오각수	 	Pn = n (3n − 1) / 2	 	1, 5, 12, 22, 35, ...
#육각수	 	Hn = n (2n − 1)	 	1, 6, 15, 28, 45, ...
#여기서 T285 = P165 = H143 = 40755 가 됩니다.

#오각수와 육각수도 되는, 그 다음으로 큰 삼각수를 구하세요.

Tide=[]
for i in range(3,7):
  for j in range(1,100000):
    p=(i-2)*j*(j-1)/2 +j
    Tide.append(int(p))
  if i==3:
    Triangle=Tide[:]
  if i==5:
    Pentagon=Tide[:]
  if i==6:
    Hexagon=Tide[:]
  Tide=[]


for i in Triangle:
  if i in Pentagon and i in Hexagon:
    print(i)
    if i>40755:
      break
