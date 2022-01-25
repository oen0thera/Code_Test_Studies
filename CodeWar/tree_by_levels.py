'''
You are given a binary tree:

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
Your task is to return the list with elements from tree sorted by levels, which means the root element goes first, then root children (from left to right) are second and third, and so on.

Return empty list if root is None.

Example 1 - following tree:

                 2
            8        9
          1  3     4   5
Should return following list:

[2,8,9,1,3,4,5]
Example 2 - following tree:

                 1
            8        4
              3        5
                         7
Should return following list:

[1,8,4,3,5,7]
'''

def tree_by_levels(node):
    result=[]
    count=0
    sets=[]
    if node==None:
      return []
    else:
      sets.append([count,node.value])
      count+=1
      sets=classify(node,result,count,sets)
      pos=0
      while len(result)<len(sets):
        for i in sets:
          if i[0]==pos:
            result.append(i[1])
        pos+=1
      return result

def classify(node,result,count,sets):
  leftNode = node.left
  rightNode = node.right
  if leftNode:
    sets.append([count,leftNode.value])
  if rightNode:
    sets.append([count,rightNode.value])
  count+=1
  if leftNode and rightNode==None:
    classify(leftNode,result,count,sets)
  elif leftNode==None and rightNode:
    classify(rightNode,result,count,sets)
  elif leftNode and rightNode:
    classify(leftNode,result,count,sets)
    classify(rightNode,result,count,sets)

  return sets
