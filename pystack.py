class Stack:
    """2020/7/13 Monday
    author:Dong Xing"""
    def __init__(self, size):
        self.stack = []
        self.top = -1

    def push(self, element):
        if self.isFull():
            raise StackException('Stack overflow.')
        else:
            self.stack.append(element)
            self.top += 1

    def pop(self):
        if self.isEmpty():
            raise StackException('Stack is empty.')
        else:
            element = self.stack[-1]
            self.top -= 1
            del self.stack[-1]
            return element

    def getTop(self):
        return self.top

    def empty(self):
        self.stack = []
        self.top = -1

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def isFull(self):
        if self.top == self.size - 1:
            return True
        else:
            return False


class StackException(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data
