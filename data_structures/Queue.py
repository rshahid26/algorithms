from .LinkedList import LinkedList


class Queue:
    def __init__(self, values=None):
        self.queue = LinkedList(values)

    def append(self, value, priority: int = 0):
        self.queue.prepend(value)

    def popleft(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.queue.remove_index(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.queue.get_index(0)

    def is_empty(self):
        return self.queue.length == 0

    def print(self):
        self.queue.print()

    @property
    def length(self) -> int:
        return self.queue.length
