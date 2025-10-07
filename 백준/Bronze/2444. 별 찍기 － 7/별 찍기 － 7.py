N = int(input())

for i in range(1,2*N):

  print(' '*abs(N-i),end='')

  print('*'*(2*N-1-abs(N-i)*2),end='')

  print()