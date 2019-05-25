# queue model
# queue follows First In First Out
import heapq
import queue

L = queue.Queue(maxsize=20)
# insert
L.put(5)
L.put(9)
L.put(1)
L.put(7)
print(L.get())


# priority Queue
class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])  # 指定字符连接成字符串

    def isEmpty(self):
        return len(self.queue) == []

    def insert(self, data):
        self.queue.append(data)

    # for poping an element based on Priority
    # return the delete element
    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item

        except IndexError:
            print()
            exit()


if __name__ == '__main__':
    myQueue = PriorityQueue()
    myQueue.insert(12)
    myQueue.insert(1)
    myQueue.insert(14)
    myQueue.insert(7)
    print(myQueue)
    while not myQueue.isEmpty():
        print(myQueue.delete())

# Heap Queue

li = [5, 7, 9, 1, 3]
# heapify : convert the iterable into heap
heapq.heapify(li)
print("\nthe created heap is", list(li))
# heappush
heapq.heappush(li, 4)
print("\nthe modified heap is", list(li))
# heappop() to pop the smallest element
print("\nthe popped element is %d" % heapq.heappop(li))



