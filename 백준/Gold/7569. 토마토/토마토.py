from collections import deque
M,N,H = [int(i) for i in input().split()]
boxes = []
for h in range(H):
  box = [list(map(int,input().split())) for _ in range(N)]
  boxes.append(box)

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dh = [0,0,0,0,1,-1]


tomatoes = 0
ripes = []
Queue = deque();

def init(graph,tomatoes):
  for h in range(H):
    for n in range(N):
      for m in range(M):
        if graph[h][n][m]==1:
          ripes.append([h,n,m,0])
          Queue.append([h,n,m,0])
          tomatoes+=1
        elif graph[h][n][m]==0:
          tomatoes+=1
  if len(ripes)==0: return -1
  return bfs(ripes[0],tomatoes)


def bfs(tom,tomatoes):
  count = 0
  tomato_count = 0
  while Queue:
    v = Queue.popleft()
    tomato_count+=1
    for i in range(len(dx)):
      if 0<=v[0]+dh[i]<H and 0<=v[1]+dy[i]<N and 0<=v[2]+dx[i]<M:
        if boxes[v[0]+dh[i]][v[1]+dy[i]][v[2]+dx[i]]==0:
          boxes[v[0]+dh[i]][v[1]+dy[i]][v[2]+dx[i]] = 1
          Queue.append([v[0]+dh[i],v[1]+dy[i],v[2]+dx[i],v[3]+1])
          count = v[3]+1
  if tomato_count!=tomatoes : return -1
  return count

print(init(boxes,tomatoes))
