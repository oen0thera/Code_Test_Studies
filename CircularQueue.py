class CircularQueue:

    def __init__(self,n):
        self.maxCount=n
        self.data=[None]*n
        self.count=0
        self.front=-1
        self.rear=-1

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count==0

    def isFull(self):
        return self.count == self.maxCount

    def enqueue(self,new):
        if self.isFull():
            raise IndexError('Queue Full')
        self.rear=(self.rear+1)%self.maxCount
        self.data[self.rear] = x
