L=[]
K=[]
M=[]
R=[]
def Solution():
  for i in range(100,1000):
    L.append(i)
    print(L)
  for a in range(1,10):
    for b in range(0,10):
      for c in range(0,10):
          K=[str(a),str(b),str(c),str(c),str(b),str(a)]
          new=''.join(K)
          print(new)
          M.append(int(new))
  print(M)
  for j in L:
    for p in L:
      if j*p in M:
        R.append(j*p)
        print(('{}x{} = {}').format(j,p,j*p))
  R.sort()
  print(R)
Solution()
