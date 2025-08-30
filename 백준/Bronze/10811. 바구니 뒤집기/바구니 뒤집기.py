N ,M =map(int,input().split())
num_list = [i for i in range(1,N+1)]
for _ in range(M):
  i,j = map(int,input().split())
  num_list=num_list[:i-1]+num_list[i-1:j][::-1]+num_list[j:]
print(' '.join([str(i) for i in num_list]))