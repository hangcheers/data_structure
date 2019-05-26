# MinHeap
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


class MaxHeap:
    def __init__(self):
        self.maxhlist = [0]
        self.currentSize = 0

    def sift_up(self, i):
        parent = i // 2
        while (parent > 0):
            if self.maxhlist[i] > self.maxhlist[parent]:
                self.maxhlist[i], self.maxhlist[parent] = self.maxhlist[parent], self.maxhlist[i]
            i = parent

    def insert(self, k):
        self.maxhlist.append(k)
        self.currentSize += 1
        self.sift_up(self.currentSize - 1)

    def sinkDown(self, i):
        child = 2 * i
        while (i * 2) <= self.currentSize:
            if child + 1 >= self.currentSize:
                mc = child  # 最大的子节点
            if child + 1 <= self.currentSize and self.maxhlist[child] < self.maxhlist[child + 1]:
                mc = child + 1
            if child + 1 <= self.currentSize and self.maxhlist[child] > self.maxhlist[child + 1]:
                mc = child
            if self.maxhlist[i] < self.maxhlist[mc]:
                self.maxhlist[i], self.maxhlist[mc] = self.maxhlist[mc], self.maxhlist[i]
            i = mc

    def delMax(self):
        retval = self.maxhlist[1]
        self.maxhlist[1] = self.maxhlist[self.currentSize]
        self.currentSize -= 1
        self.maxhlist.pop()
        self.sinkDown(1)
        return retval

    def buildMH(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.maxhlist = [0] + alist[:]
        while i > 0:
            self.sinkDown(i)
            i -= 1

# MaxHeap
maxHeap = MaxHeap()
maxHeap.buildMH([10, 5, 6, 2, 3])
print(maxHeap.delMax())
print(maxHeap.delMax())
print(maxHeap.delMax())
