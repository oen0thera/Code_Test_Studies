'''파이썬에서 병합정렬 구현'''
'''홀수부분 따로 구현안됨'''

List=[8,2,4,3,5,1,6,7]
#for _ in range(int(input())):
  #List.append(int(input()))

def MergeSort(target:list,first:int,last:int):
  mid = first+last//2
  if first==mid or mid==last:
    return

  print(first,mid,last)
  print(target)
  if mid>0:
    MergeSort(target,first,mid)
    Merger(target,first,mid,last)
    MergeSort(target,mid,last)
    Merger(target,first,mid,last)

  print(target,first,mid,last)

def Merger(target,first,mid,last):
  result=[]
  left=target[first:mid]
  right=target[mid:last]
  left_num=0
  right_num=0
  while left_num!=len(left) or right_num!=len(right):
    if left_num<len(left) and right_num<len(right) and left[left_num]<=right[right_num] and left[left_num] not in result:
      result.append(left[left_num])
      left_num+=1
    elif left_num<len(left) and right_num<len(right) and left[left_num]>right[right_num] and right[right_num] not in result:
      result.append(right[right_num])
      right_num+=1
    else:
      if right_num>left_num:
        result.append(left[left_num])
        left_num+=1
      elif right_num<left_num:
        result.append(right[right_num])
        right_num+=1
    print(result)

  target[first:last]=result
  print(left,right)

MergeSort(List,0,len(List))
