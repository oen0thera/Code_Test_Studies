class MaxHeap:
    def __init__(self):
        self.data = [None]

    def remove(self):
        if len(self.data)>1:
                self.data[1], self.data[-1] = self.data[-1],self.data[1]
                data = self.data.pop(-1)
                self.maxHeapify(1)

        else:
            data = None

        return data

    def maxHeapify(self,i):
        left = i*2
        right = (i*2)+1
        smallest = i
        if left<len(self.data) and self.data[left]>self.data[i]:
            smallest = left
        if right<len(self.data) and self.data[right]>self.data[i]:
            smallest = right

        if smallest!=i:
            i,smallest = smallest,i
            self.maxHeapify(smallest)
