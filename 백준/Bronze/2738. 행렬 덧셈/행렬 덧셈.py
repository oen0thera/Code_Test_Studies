M,N = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(M)]
for i in range(M):
  col = list(map(int,input().split()))
  for j in range(len(col)):
    A[i][j]+=col[j]

for r in A :
  print(' '.join([str(i) for i in r]))