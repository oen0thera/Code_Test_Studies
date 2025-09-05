N = int(input())
maps = [list(map(int,input().split())) for i in range(N) ]
blue = 0
white = 0
def divider(graph):
  global blue,white
  for i in range(0,len(graph),len(graph)//2):
    for j in range(0,len(graph),len(graph)//2):
      divided_graph = [row[j:j+len(graph)//2] for row in graph[i:i+len(graph)//2]]
      scanned = scan(divided_graph)
      if scanned==False:
        divider(divided_graph)
      else:
        if divided_graph[0][0]==0:
          white+=1
        else:
          blue+=1


def scan(graph):
    first = graph[0][0]
    for row in graph:
        for cell in row:
            if cell != first:
                return False
    return True

if scan(maps):
  if(maps[0][0]==0):
    white+=1
  else:
    blue+=1
else:
  divider(maps)
print(white)
print(blue)