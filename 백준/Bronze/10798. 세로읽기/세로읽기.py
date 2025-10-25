graph = [[i for i in input()] for _ in range(5)]
max_len = max(len(i) for i in graph)
for i in range(max_len):
  for j in range(len(graph)):
    try:
      print(graph[j][i],end='')
    except:
      pass