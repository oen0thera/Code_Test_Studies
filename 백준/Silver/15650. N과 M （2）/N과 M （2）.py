N,M = [int(i) for i in input().split()]

def b_track(i,j,arr=[False for _ in range(N)]):
  if N==M:
     print(*[i+1 for i in range(N)])
     return
  if i<N:
    if i==N-1 and j==N-1: return
    if arr.count(True)==M: 
      print(*[i+1 for i in list(filter(lambda x: arr[x]==True,range(len(arr))))])
      
      return
    if j<N and arr[j]==False:
      arr[j]=True
      b_track(i,j+1,arr)
      arr[j]=False
      b_track(i,j+1,arr)
    else:
      return
    

b_track(0,0)