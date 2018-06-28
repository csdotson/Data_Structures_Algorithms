class Queue:
    """ Implementation of Queue object """
    def __init__(self):
        self._queue = []
    
    def empty(self):
        return len(self._queue) == 0

    def enqueue(self, val):
        self._queue.append(val)

    def dequeue(self):
        if self.empty():
            raise IndexError('dequeue(): Queue is empty')
        return self._queue.pop(0)

    def peek_first(self):
        return self._queue[0]

    def peek_last(self):
        return self._queue[-1]

    def max(self):
        if self.empty():
            raise IndexError('max(): Queue is empty')
        return max(self._queue)
