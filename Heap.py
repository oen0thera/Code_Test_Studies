class MaxHeap:

    def __init__(self):
        self.data = [None]


    def insert(self, item):
        self.data.append(item)
        curr = self.data.index(item)
        parent = self.data[curr//2]
        print(parent)
        print('hi')
        while parent!=None:
            curr = self.data.index(item)
            parent = self.data[curr//2]
            if self.data[curr//2] and self.data[curr]>self.data[curr//2]:
                    self.data[curr],self.data[curr//2]=self.data[curr//2],self.data[curr]
                    print(self.data[curr])
                    print(self.data)
                    print('changing pos')
                    print(parent)
            else:
                    break
        print(self.data)
L=MaxHeap()
L.insert(32)
L.insert(33)
L.insert(44)
L.insert(55)
L.insert(12)
L.insert(66)

L.remove()
