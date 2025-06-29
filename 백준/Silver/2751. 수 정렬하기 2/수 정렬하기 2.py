num_list = []
for _ in range(int(input())):
  num_list.append(int(input()))
  

def merge(list,left,mid,right):
  i=left
  j=mid+1
  sorted=[]
  while(i<=mid and j<=right):
    if list[i]<list[j]:
      sorted.append(list[i])
      i+=1
    else:
      sorted.append(list[j])
      j+=1
  if i>mid:
    for r in range(j,right+1):
      sorted.append(list[r])
  else:
    for r in range(i,mid+1):
      sorted.append(list[r])
  for r in range(len(sorted)):
    num_list[left+r] = sorted[r]


def merge_sort(list,left,right):
  mid = (left+right)//2
  if(left<right):
    merge_sort(list,left,mid)
    merge_sort(list,mid+1,right)
    merge(list,left,mid,right)
    
merge_sort(num_list,0,len(num_list)-1)

for i in num_list:
  print(i)