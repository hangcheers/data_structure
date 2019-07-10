# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data or len(data) == 0: return 0
        n = len(data)
        first = self.GetFirstK(data, k, 0, n-1)
        last = self.GetLastK(data, k, 0, n-1)
        if first > -1 and last > -1:
            return last - first + 1
        return 0
    
    def GetFirstK(self, data, k, start, end):
        if start > end: return -1
        while start <= end:
            mid = start + (end - start)//2
            if (data[mid] == k):
                if (mid > start and data[mid - 1] != k) or mid == start:
                    return mid
                else:
                    end = mid - 1
            else:
                if data[mid] > k:
                    end = mid - 1
                else:
                    start = mid + 1
        

    def GetLastK(self, data, k, start, end):
        if start > end: return -1
        while start <= end:
            mid = start + (end - start)//2
            if (data[mid] == k):
                if (mid< end and data[mid + 1]!=k) or mid == end: 
                    return mid
                else:
                    start = mid + 1
            else:
                if data[mid] > k:
                    end = mid - 1
                else:
                    start = mid + 1
        
    
   
