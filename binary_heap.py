class MinHeap:
    def __init__(self):
        self.heaplist = [0]
        self.currentSize = 0

    def bubble(self, i):
        while (i // 2 > 0):
            if self.heaplist[i] < self.heaplist[i // 2]:  # i//2 means parent node
                self.heaplist[i], self.heaplist[i // 2] = self.heaplist[i // 2], self.heaplist[i]
            i = i // 2

    def insert(self, k):
        self.heaplist.append(k)
        self.currentSize += 1
        self.bubble(self.currentSize)

    def sinkDown(self, i):
        """
        :left child index: 2*i, right child index: 2*i+1, parent index: i//2
        """
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)  # 最小的子节点
            if self.heaplist[i] > self.heaplist[mc]:
                self.heaplist[i], self.heaplist[mc] = self.heaplist[mc], self.heaplist[i]
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heaplist[i * 2] < self.heaplist[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentSize]
        self.currentSize -= 1
        self.heaplist.pop()
        self.sinkDown(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heaplist = [0] + alist[:]
        while (i > 0):
            self.sinkDown(i)
            i = i - 1


minHeap = MinHeap()
minHeap.buildHeap([9, 5, 6, 2, 3])
print(minHeap.delMin())
print(minHeap.delMin())
