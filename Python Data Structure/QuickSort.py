
'''파이썬에서 퀵정렬 구현'''
'''불완전 정렬임에 유의'''

List=[]
for _ in range(int(input())):
  List.append(int(input()))

def insertionSort(target:list, first:int, last:int):
  if first<last:
    insertionSort(target,first,last-1)
    insertInOrder(target[last],target,first,last-1)

def insertInOrder(anEntry:int, target:list, begin:int, end:int ):
  if anEntry>=target[end]:
    target[end+1] = anEntry
  elif begin<end:
    target[end+1] = target[end]
    insertInOrder(anEntry,target,begin,end-1)
  else:
    target[end+1] = target[end]
    target[end] = anEntry

def quickSort(target:list, first:int, last: int):
  MIN_SIZE=4
  if last-first+1<MIN_SIZE:
    insertionSort(target,first,last)
  else:

    pivotIndex = partition(target,first,last)
    quickSort(target,first,pivotIndex-1)
    quickSort(target,pivotIndex+1,last)

def sortFirstMiddleLast(target:list, first:int, middle:int,last:int):
  while not (target[first]<=target[middle] and target[middle]<=target[last]):
    if target[first]>target[middle]:
      swap(target,first,middle)
    if target[middle]>target[last]:
      swap(target,middle,last)
    if target[first]>target[last]:
      swap(target,first,last)
    if target[first]<=target[middle] and target[middle]<=target[last]:
      return

def partition(target:list,first:int,last:int):
  mid = len(target)//2
  sortFirstMiddleLast(target,first,mid,last)
  swap(target,mid,last-1)
  print(target)
  pivotIndex=last-1
  pivotValue = target[pivotIndex]
  indexFromLeft = first+1
  indexFromRight = last-2
  done = False
  while done==False:
    while target[indexFromLeft]<pivotValue:
      indexFromLeft+=1
    while target[indexFromRight]>pivotValue:
      indexFromRight-=1
    if indexFromLeft<indexFromRight:
      swap(target,indexFromLeft,indexFromRight)
      print(target)
      indexFromLeft+=1
      indexFromRight-=1
    else:
      done=True
  swap(target,pivotIndex,indexFromLeft)
  print(target,pivotIndex,indexFromLeft)
  pivotIndex = indexFromLeft
  return pivotIndex

def swap(target:list,i:int,j:int):
  temp = target[i]
  target[i] = target[j]
  target[j] = temp


quickSort(List,0,len(List)-1)
