# implement stack using arrays
from sys import maxsize


def createStack():
    stack = []
    return stack


def isEmpty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    print(item + "pushed to stack")


def pop(stack):
    if (isEmpty(stack)):
        return str(-maxsize - 1)  # return minus infinite

    return stack.pop()


stack = createStack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
print(pop(stack) + "popped from stack")


# implement stack using linked list
class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return True if self.head is None else False

    def push(self, data):
        newNode = StackNode(data)
        newNode.next = self.head
        self.head = newNode
        print("%d pushed to stack" % (data))

    def pop(self):
        if (self.isEmpty()):
            return float("-inf")
        temp = self.head
        self.head = self.head.next
        return temp.data


stack = Stack()
print("\n")
stack.push(60)
stack.push(40)
stack.push(50)
print("%d poped from stack" % (stack.pop()))
