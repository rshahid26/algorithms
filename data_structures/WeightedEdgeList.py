class Node:
    def __init__(self, val, weight):
        self.next = None
        self.val = val
        self.weight = weight


class WeightedEdgeList:
    def __init__(self, val=None, weight: int = None):
        if val is not None:
            self.head = Node(val, weight)
            self._length = 1
        else:
            self.head = None
            self._length = 0

    @property
    def degree(self):
        return self._length

    def append(self, val, weight: int = None) -> None:
        if self.head is None:
            self.head = Node(val, weight)
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = Node(val, weight)
        self._length += 1

    def prepend(self, val, weight: int = None):
        head = Node(val, weight)
        head.next = self.head

        self.head = head
        self._length += 1

    def remove(self, target_val) -> None:
        if self.head is None:
            return

        while self.head.val == target_val:
            self.head = self.head.next

        current = self.head
        while current.next is not None:
            if current.next.val == target_val:
                current.next = current.next.next
                self._length -= 1
            else:
                current = current.next
        self._length -= 1

    def print(self) -> None:
        current = self.head

        while current is not None:
            print(current.val, end="")
            current = current.next
        print()

    def print_weights(self) -> None:
        current = self.head

        while current is not None:
            print(current.weight, end="")
            current = current.next
        print()