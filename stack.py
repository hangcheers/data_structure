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


# reverse the string using stack
def createStack():
    stack = []
    return stack


def size(stack):
    return len(stack)


def isEmpty(stack):
    if len(stack) == 0:
        return True


def push(stack, item):
    stack.append(item)
    # print(item + "pushed to stack")


def pop(stack):
    if isEmpty(stack): return
    return stack.pop()


def reverse(string):
    n = len(string)
    stack = createStack()
    for i in range(0, n, 1):
        push(stack, string[i])
    string = ""
    for i in range(0, n, 1):
        string += pop(stack)
    return string


string = "Geeks"
string = reverse(string)
print(string)


