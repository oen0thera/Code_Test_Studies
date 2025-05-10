N=int(input())
for i in range(0,N):
  for j in range(0,N):
    if (abs(j-(N-1))<=i):
      print('*',end='')
    else:
      print(' ',end='')
  print()