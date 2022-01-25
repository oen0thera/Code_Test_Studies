class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1


    def depth(self):
        countleft=1
        countleft+=self.left.depth() if self.left else 0
        countright=1
        countright+=self.right.depth() if self.right else 0
        if countright>countleft:
                return countright
        elif countright<countleft:
                return countleft
        else:
                return countleft

    def __str__(self):
        return 'str:{}'.format(self.data)
class BinaryTree:

    def __init__(self, r):
        self.root = r

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0


    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0


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


print(a.depth())
print(a.size())
L=BinaryTree(a)
print(L.depth())
print(a)
