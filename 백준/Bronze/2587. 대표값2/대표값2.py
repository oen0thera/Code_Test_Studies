num_list=[]
while True:
  try:
    num = int(input())
    num_list.append(num)
  except EOFError:
    break

def swap(a,b):
  return b,a


def sort(num_list):
  index= 0
  while index<len(num_list)-1:
    if len(num_list)==1: 
      return (num_list[index],num_list[index])
    if num_list[index]>num_list[index+1]:
      num_list[index],num_list[index+1] = swap(num_list[index],num_list[index+1])
      index=0
    else:
      index+=1
      
  return sum(num_list)//len(num_list), num_list[len(num_list)//2]

avg, med = sort(num_list)
print(avg)
print(med)
