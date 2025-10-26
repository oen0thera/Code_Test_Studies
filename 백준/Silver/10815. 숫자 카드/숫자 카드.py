N = int(input())
own = set(map(int,input().split()))
M = int(input())
tar = set(map(int,input().split()))
intersect = own&tar
for i in tar:
  if i in intersect:
    print(1, end=' ')
  else:
    print(0, end=' ')