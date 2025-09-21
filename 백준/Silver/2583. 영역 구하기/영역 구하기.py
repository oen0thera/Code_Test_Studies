from collections import deque

N,M,K = map(int,input().split())
graph = [[False]*M for _ in range(N)]
for _ in range(K):
  x1,y1,x2,y2 = map(int,input().split())
  for i in range(y1,y2):
    for j in range(x1,x2):
      graph[i][j] = True

count = 0
def bfs(sr,sc):
  q = deque([(sr,sc)])
  graph[sr][sc]=True
  count=1
  while q:
    r,c = q.popleft()
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
      dr,dc = r+dx, c+dy
      if 0<=dr<N and 0<=dc<M and graph[dr][dc]==False:
        graph[dr][dc] = True
        count+=1
        q.append((dr,dc))
  return count
  
total_count = []
for i in range(N):  
  for j in range(M):
    if graph[i][j]==False:
      total_count.append(bfs(i,j))
print(len(total_count))
print(' '.join([str(i) for i in sorted(total_count)]))