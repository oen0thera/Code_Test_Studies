N,M = map(int,input().split())
num_list = [str(i) for i in list(map(int,input().split())) if i<M]
print(' '.join(num_list))