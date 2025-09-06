def quicksort(arr):
  if len(arr)<=1:
    return arr
  pivot = arr[0]
  left= [x for x in arr[1:] if x<=pivot]
  right= [x for x in arr[1:] if x>pivot]
  return quicksort(right) + [pivot] + quicksort(left)

N , k = map(int,input().split())
num_list = list(map(int,input().split()))

sorted_list = quicksort(num_list)
print(sorted_list[k-1])
