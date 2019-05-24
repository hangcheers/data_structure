import numpy as np


def linearSearch(arr, n, x):
    for i in range(n):
        if (arr[i] == x):
            return i
    return -1


# iterative
def binarySearch(arr, l, r, x):
    while l < r:
        mid = int(l + (r - 1) / 2)
        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            l = mid + 1

        else:
            r = mid - 1
    return -1


# recursive
def binarySearch_r(arr, l, r, x):
    if l <= r:
        mid = int(l + (r - l) // 2)
        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binarySearch_r(arr, l, mid - 1, x)

        else:
            return binarySearch_r(arr, mid + 1, r, x)
    else:
        return -1


arr = np.array([2, 3, 4, 10, 40, 80])
x = 50
l = 0
r = arr.shape[0] - 1
result = binarySearch(arr, l, r, x)
if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in array")