N, M = map(int,input().split())

num_list = [i+1 for i in range(N) ]

def swap(a,b):
  a,b = b,a
  return a,b

for _ in range(M):
  a, b= map(int,input().split())
  num_list[a-1],num_list[b-1] = swap(num_list[a-1],num_list[b-1])

print(' '.join([str(i) for i in num_list]))