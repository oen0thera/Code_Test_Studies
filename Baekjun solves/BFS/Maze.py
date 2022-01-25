import sys
col,row = map(int,input().split())
data = []
shape=data[1:]
col= int(size[0])
row= int(size[1])

Matrix = []
Visited = []

for i in shape:
    Matrix.append([j for j in i])

Visited.append([0,0,0])
def BFS(Visited):
    Node = Visited[0]
    if Node[0]==row-1:
        rightNode=None
    else:
        rightNode = [Node[0]+1,Node[1],Node[2]]
    if Node[1]==col-1:
        lowerNode=None
    else:
        lowerNode = [Node[0],Node[1]+1,Node[2]]

    if rightNode!=None:
        rightNodeValue=Matrix[rightNode[0]][rightNode[1]]
        rightNode[2]=rightNode[2]+int(rightNodeValue)
        Visited.append(rightNode)
    else:
        pass
    if lowerNode!=None:
        lowerNodeValue=Matrix[lowerNode[0]][lowerNode[1]]
        lowerNode[2]=lowerNode[2]+int(lowerNodeValue)
        Visited.append(lowerNode)
    else:
        pass
    Visited.remove(Node)



while True:
    if Visited[0][0]==row-1 and Visited[0][1]==col-1:
        print(sorted(Visited, key=lambda x: x[2])[0][2])
        break
    else:
        BFS(Visited)
