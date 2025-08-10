num_list = []
for i in range (9):
  num_list.append(int(input()))
max_index = [i for i,v in enumerate(num_list) if v==max(num_list)].pop()
print(num_list[max_index])
print(max_index+1)