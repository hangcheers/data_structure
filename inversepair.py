class Solution:
    def InversePairs(self, data):
        n = len(data)
        if not data or n == 0: return 0
        copy = [i for i in data]
        count = self.MergeSort(data, copy, 0, n-1)
        return count % 1000000007
    
    def MergeSort(self,data, copy, start, end):
        if start == end:
            copy[start] = data[start]
            return 0
        mid = (start + end)//2
        leftcount = self.MergeSort(data, copy, start, mid)
        rightcount = self.MergeSort(data, copy, mid + 1, end)
        count = 0
        i = mid  # 前子数组的尾端
        j = end  # 后子数组的尾端
        copy_index = end # 比较结果放入辅助数组的尾端
        
        # 归并排序：将两个有序数组合并为一个有序表
        while (i >= start) and (j >= mid +1):
            if data[i] > data[j]:# 前面的子数组的数 > 后面的子数组的数
                copy[copy_index] = data[i]
                i -= 1
                count = count + j - mid
            else:
                copy[copy_index] = data[i]
                j -= 1
            copy_index -= 1 
                
        while i >= start:
            copy[copy_index] = data[i]
            i -= 1 
            copy_index -= 1
        
        while j >= mid + 1:
            copy[copy_index] = data[j]
            j -= 1 
            copy_index -= 1 
        for i in range(start,end+1):
            data[i] = copy[i]
        
        return leftcount + rightcount + count
        
a = Solution()
data = [1, 2, 3, 4, 0]

print(a.InversePairs(data))
        
                
        
            
