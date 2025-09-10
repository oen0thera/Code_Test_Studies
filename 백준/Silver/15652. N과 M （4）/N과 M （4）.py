import sys
sys.setrecursionlimit(100000)

M, N = map(int,input().split())

nums = []

def recursive_search(curr=[],i=0,length=N):
  if len(curr)<N:
    curr.append(i+1)
    recursive_search(curr,i,N)
  else:
    print(' '.join([str(i) for i in curr]))
    while curr:
      prev = curr.pop()
      if prev<M:
        recursive_search(curr,prev)
        break
    

recursive_search([],0,N)
