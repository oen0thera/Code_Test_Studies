N, M = map(int,input().split())


num_list = [0 for i in range(N)]
for _ in range(M):
  i,j,k = map(int,input().split())
  for t in range(i,j+1):
    num_list[t-1]=k
print(' '.join([str(i) for i in num_list]))