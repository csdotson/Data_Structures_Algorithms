class Stack:
    """ Implementation of Stack object """
    def __init__(self):
        self._stack = []

    def empty(self):
        return len(self._stack) == 0

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        return self._stack.pop()

    def push(self, val):
        self._stack.append(val)

    def peek(self):
        return self._stack[-1]

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        max = 0
        for i in self._stack:
            if i > max:
                max = i
        return max

    def size(self):
        return len(self._stack)

    