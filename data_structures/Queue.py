from .LinkedList import LinkedList


class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def append(self, item, priority: int = 0):
        self.queue.prepend(item)

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
    def size(self) -> int:
        return self.queue.length
