def quicksort(arr,left,right):
  if left<right:
    pivotIndex = partition(arr,left,right)
    quicksort(arr,left,pivotIndex-1)
    quicksort(arr,pivotIndex+1,right)

def partition(arr,left,right):
  pivot = arr[right]
  index = left-1
  for i in range(left,right):
    if arr[i] >= pivot:
      index +=1
      arr[i],arr[index] = swap(arr[i],arr[index])
      
  arr[index+1],arr[right] = swap(arr[index+1],arr[right])
  return index+1

def swap(a,b):
  return b,a

arr = [int(i) for i in input()]
quicksort(arr,0,len(arr)-1)
print(''.join([str(i) for i in arr]))