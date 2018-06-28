class Stack:
    """ Implementation of Stack object """
    def __init__(self):
        self.stack = []

    def empty(self):
        return len(self.stack) == 0

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        return self.stack.pop()

    def push(self, val):
        return self.stack.append(val)

    def peek(self):
        return self.stack[-1]

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        max = 0
        for i in self.stack:
            if i > max:
                max = i
        return max

    def size(self):
        return len(self.stack)

    