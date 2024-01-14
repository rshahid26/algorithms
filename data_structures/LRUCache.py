from .LinkedList import Node


class DoubleNode(Node):
    def __init__(self, key, val) -> None:
        super().__init__(val)
        self.key = key
        self.prev = None

class LRUCache:
    def __init__(self, size: int) -> None:
        if size <= 0:
            raise ValueError("Size must be greater than zero.")
        self._size = size
        self.table = {}
        self.LRU = None  # head
        self.MRU = None  # tail

    def put(self, key, val) -> None:
        if key in self.table:
            node = self.table[key]
            node.val = val
            self._update_rank(node)
            return

        if len(self.table) == self._size:
            del self.table[self.LRU.key]
            self._remove(self.LRU)

        self._add(DoubleNode(key, val))

    def get(self, key):
        if key not in self.table:
            return -1

        node = self.table[key]
        self._update_rank(node)
        return node.val

    def set_size(self, size: int) -> None:
        if size <= 0:
            raise ValueError("size must be greater than zero.")
        self._size = size
        while len(self.table) > self._size:
            del self.table[self.LRU.key]
            self._remove(self.LRU)
        

    def _update_rank(self, node: DoubleNode) -> None:
        self._remove(node)
        self._add(node)

    def _add(self, node: DoubleNode) -> None:
        if not self.MRU:
            self.MRU = self.LRU = node
        else:
            self.MRU.next = node
            node.prev = self.MRU
        self.MRU = node
        self.table[node.key] = node

    def _remove(self, node: DoubleNode):
        # If node is at the beginning (LRU)
        if node.prev is None:
            self.LRU = node.next
        else:
            node.prev.next = node.next
            
        # If node is at the end (MRU)
        if node.next is None:
            self.MRU = node.prev
        else:
            node.next.prev = node.prev

        node.next = node.prev = None

    def print_cache(self) -> None:
        current = self.LRU
        while current:
            print(f"Key: {current.key}, Val: {current.val}", end=" -> ")
            current = current.next
        print("END")
