from .Queue import Queue
from .LinkedList import Node


class PriorityQueue(Queue):
    def __init__(self):
        super().__init__()

    def append(self, value, priority: int = 0):
        # Using a selection sort with array gives O(n) sorted insert
        element = {"value": value, "priority": priority}
        current = self.queue.head

        if current is None:
            self.queue.append(element)
            return
        if priority < current.val["priority"]:
            self.queue.prepend(element)
            return

        while current.next is not None:
            if current.next.val["priority"] > priority:
                temp = current.next
                new_node = Node(element)
                current.next = new_node
                new_node.next = temp
                self.queue._length += 1
                return
            current = current.next
        self.queue.append(element)

    def popleft(self):
        return super().popleft()["value"]

    def list_values(self) -> list:
        values = []
        current = self.queue.head
        while current is not None:
            values.append(current.val["value"])
            current = current.next
        return values
    
    def list_priorities(self) -> list:
        priorities = []
        current = self.queue.head
        while current is not None:
            priorities.append(current.val["priority"])
            current = current.next
        return priorities
    
    def print(self):
        current = self.queue.head
        while current is not None:
            print(current.val["value"], end=" ")
            current = current.next
        print()
    
    def print_elements(self):
        current = self.queue.head
        while current is not None:
            print(current.val, end=" ")
            current = current.next
        print()
