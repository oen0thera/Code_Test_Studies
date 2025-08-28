num_list = []
rest = []
while True:
  try:
    num_list.append(int(input()))
  except EOFError:
    break
for i in num_list:
  if i%42 not in rest:
    rest.append(i%42)

print(len(rest))