# 升序
# iteratively
def bubbleSort(arr):
    n = len(arr)
    # traverse through all array elements
    for i in range(n):
        for j in range(0, n - i - 1):
            # traverse the array from 0 to n-i-1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print("bubble sorted arr")
print([arr[i] for i in range(len(arr))])


# recursively
# do one pass of normal bubble sort
# recur for all elements last of current subarray
def bubble_sort(listt):
    for i, num in enumerate(listt):
        try:
            if listt[i + 1] < num:
                listt[i], listt[i + 1] = listt[i + 1], num
                bubbleSort(listt)
        except IndexError:
            pass
    return listt


# selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        minimal = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimal]:
                minimal = j
        arr[minimal], arr[i] = arr[i], arr[minimal]
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort(arr)
print("selection sorted array")
print([arr[i] for i in range(len(arr))])


# insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        while arr[j] > arr[j + 1] and j >= 0:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j = j - 1
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr)
print("insertion sorted array")
print([arr[i] for i in range(len(arr))])


# quick sort
# divide and conquer
def quickSort(alist, first, last):
    if first < last:
        spilt_pt = partition(alist, first, last)  # split point
        quickSort(alist, first, spilt_pt - 1)  # left
        quickSort(alist, spilt_pt + 1, last)  # right


def partition(alist, first, last):
    pivot = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivot:
            leftmark = leftmark + 1

        while leftmark <= rightmark and alist[rightmark] >= pivot:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    alist[first], alist[rightmark] = alist[rightmark], alist[first]
    return rightmark


arr = [64, 34, 25, 12, 22, 11, 90]
first = 0
last = len(arr) - 1
quickSort(arr, first, last)
print("quick sorted array")
print([arr[i] for i in range(len(arr))])
