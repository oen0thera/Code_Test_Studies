[R,C] = [int(i) for i in input().split()]
graph = [[i for i in input()] for _ in range(R)]

Q = [False for _ in range(26)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

result = 0

def dfs(r,c,count):
  global result
  result = max(count,result)
  for k in range(4):
    nx = r+dx[k]
    ny = c+dy[k]
    if 0<=nx<R and 0<=ny<C:
      if Q[ord(graph[nx][ny])-ord('A')]==False:
        Q[ord(graph[nx][ny])-ord('A')]=True
        dfs(nx,ny,count+1)
        Q[ord(graph[nx][ny])-ord('A')]=False
        

Q[ord(graph[0][0])-ord('A')]=True
dfs(0,0,1)
print(result)