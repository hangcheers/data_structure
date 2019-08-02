# -*- coding:utf-8 -*-
# 左边是最大堆，右边是最小堆。
# 保障数据的平均分配，左右两边的数据相差1
# 数据的总数目是偶数时，新加入的数据先插入最大堆，经过筛选后，将选出的最大堆的最大元素插入小根堆。
# 数据的总数目是奇数时，新加入的数据先插入最小堆，经过筛选后，将选出的最小堆的最小元素插入大根堆。
# 保证最大堆的最大的数小于最小堆的最小元素
# 如果当前数目是偶数，取最小堆和最大堆根结点的平均值，如果当前数目是奇数，取最小堆的根结点
# 这个方法利用的是priority queue，当插入元素或者删除元素的时候，队列会自动进行调整，保证队首元素
#一定是优先权最大/最小的。
from heapq import *
class Solution:
    def __init__(self):
        self.minNums = []
        self.maxNums = []
    
    def maxHeapInsert(self, num):
        self.maxNums.append(num)
        lens = len(self.maxNums)
        i = lens - 1
        while i > 0:
            if self.maxNums[i] > self.maxNums[(i-1)//2]:
                self.maxNums[i], self.maxNums[(i-1)//2] = self.maxNums[(i-1)//2], self.maxNums[i]
            else:
                break
                
    def maxHeapPop(self):
        t = self.maxNums[0]
        self.maxNums[0],self.maxNums[-1] = self.maxNums[-1], self.maxNums[0]
        self.maxNums.pop()
        lens = len(self.maxNums)
        i = 0
        while 2*i + 1 < lens:
            nexti = 2*i + 1
            if (nexti + 1 < lens) and (self.maxNums[nexti + 1] > self.maxNums[nexti]):
                nexti += 1
            if self.maxNums[nexti] > self.maxNums[i]:
                self.maxNums[nexti], self.maxNums[i] = self.maxNums[i], self.maxNums[nexti]
            else:
                break
        return t
    
    def Insert(self, num):
        n = len(self.minNums) + len(self.maxNums)
        if n & 1 == 0:
            if len(self.maxNums) > 0 and num < self.maxNums[0]:
                self.maxHeapInsert(num)
                num = self.maxHeapPop()
            heappush(self.minNums, num)
        else:
            if len(self.minNums) > 0 and num > self.minNums[0]:
                num = heappushpop(self.minNums, num)
            self.maxHeapInsert(num)
            
    def GetMedian(self, n = None):
        all_n = len(self.minNums) + len(self.maxNums)
        if all_n == 0:
            return -1
        if (all_n & 1):
            return self.minNums[0]
        else:
            return (self.maxNums[0] + self.minNums[0])/2.0

# [5,2,3,4,1,6,7,0,8]
# 5.00 3.50 3.00 3.50 3.00 3.50 4.00 3.50 4.00
s = Solution()
s.Insert(5)
print(s.GetMedian())
s.Insert(2)
print(s.GetMedian())
s.Insert(3)
print(s.GetMedian())
s.Insert(4)
print(s.GetMedian())
s.Insert(1)
print(s.GetMedian())
s.Insert(6)
print(s.GetMedian())
s.Insert(7)
print(s.GetMedian())
s.Insert(0)
print(s.GetMedian())
s.Insert(8)
print(s.GetMedian())

            
            
