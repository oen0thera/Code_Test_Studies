st_list = [i for i in range(1,31)]
while True:
  try:
    del st_list[st_list.index(int(input()))]
  except EOFError:
    break
print(st_list[0])
print(st_list[len(st_list)-1])
