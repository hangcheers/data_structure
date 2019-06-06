class Stack:
    def __init__(self):
        self.items = []
        self.length = 0

    # insert
    def push(self,val):
        self.items.append(val)
        self.length += 1

    def empty(self):
        return self.length == 0

    # delete
    def pop(self):
        if self.empty():
            return None
        self.length -= 1
        return self.items.pop()

    def peek(self):
        if self.empty():
            return None
        return self.items[0]

precedence = {'*':3,'/':3,'+':2,'-':2,'(':1}

def convert(expression):
    print(__convert(expression.split()))

def __convert(tokens):
    stack = Stack()
    res = [] # store the string

    for token in tokens:
        if token.isalpha():
            res.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while True:
                temp = stack.pop()
                if temp is None or temp == '(':
                    break
                elif not temp.isalpha():
                    res.append(temp)
        else: # must be operator
            if not stack.empty():
                temp = stack.peek()
                while not stack.empty() and precedence[temp] >= precedence[token] and token.isidentifier():
                    res.append(stack.pop())
                    temp = stack.peek()
            stack.push(token)

    # the rest
    while not stack.empty():
        res.append(stack.pop())
    return res

convert("A * ( B + C ) + D")