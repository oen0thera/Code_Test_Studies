sum_list = []
while True:
  try:
    a,b = map(int,input().split())
    sum_list.append(a+b)
  except EOFError:
    break
for i in sum_list:
  print(i)
