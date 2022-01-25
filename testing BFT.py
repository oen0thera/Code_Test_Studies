class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, r):
        self.root = r


    def bft(self):
        traversal=[]
        Q=ArrayQueue()
        if self.root:
            Q.enqueue(self.root)
            while Q.isEmpty()==False:
                gore=Q.dequeue()
                traversal.append(gore.data)
                if gore.left:
                    Q.enqueue(gore.left)
                if gore.right:
                    Q.enqueue(gore.right)
        else:
            return 0

        return traversal


def solution(x):
    return 0

a=Node(6)
b=Node(7)
c=Node(8)
d=Node(9)
e=Node(10)
f=Node(11)
g=Node(12)
a.left= b
a.right= c
b.right=e
b.left=d
c.left=f
f.right=g

L=BinaryTree(a)

print(L.bft())
