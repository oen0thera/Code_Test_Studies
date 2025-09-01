graph = []
for _ in range(9):
  graph.append(list(map(int,input().split())))

max=-1
pos = (1,1)
for i in range(9):
  for j in range(9):
    if graph[i][j]>max:
      max=graph[i][j]
      pos = (i+1,j+1)

print(max)
print(pos[0],pos[1])
    