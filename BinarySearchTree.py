class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


    def insert(self, key, data):
        if key<self.key:
            if self.left == None:
                self.left= Node(key,data)
                print(self.left.key)
            else:
                self.left.insert(key,data)
        elif key>self.key:
            if self.right == None:
                self.right= Node(key,data)
                print(self.right.key)
            else:
                self.right.insert(key,data)
        else:
            raise KeyError ('NoRepeatedDataAllowed')

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal


class BinSearchTree:

    def __init__(self):
        self.root = None


    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)

        else:
            self.root = Node(key, data)


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

def solution(x):
    return 0

L=BinSearchTree()
L.insert(9,'A')
L.insert(7,'B')
L.insert(11,'C')
L.insert(6,'D')
L.insert(8,'E')
L.insert(10,'F')
L.insert(12,'G')

for i in L.inorder():
    print(i.data)
