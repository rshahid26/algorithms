import math
from PriorityQueue import PriorityQueue


class MinHeap:

    def __init__(self, elements: list = None):
        self.array = [dict]  # index elements at 1
        self._OFFSET = len(self.array)
        self._slow_init(elements)

    def _fast_init(self, elements):
        # Initializes a heap in O(n) time using heapify_down
        # TODO: Fix this
        if elements is not None:
            for item, priority in elements:
                element = {"item": item, "priority": priority}
                self.array.append(element)

            # runs O(2n) times
            for i in range(self.size // 2, self._OFFSET - 1, -1):
                self._heapify_down(i)

    def _slow_init(self, elements):
        # Initializes a heap in O(nlogn) time using heapify_up
        if elements is not None:
            for item, priority in elements:
                self.append(item, priority)

    @property
    def size(self):
        return len(self.array) - self._OFFSET

    def append(self, item, priority: int):
        element = {"item": item, "priority": priority}
        self.array.append(element)
        self._heapify_up(len(self.array) - 1)

    def _heapify_up(self, index: int):
        if self._parent_index(index) == 0:
            return  # root added to heap

        if self.get_parent(index)["priority"] > self.array[index]["priority"]:
            # Swap values of parent and child elements
            self._swap_elements(index, self._parent_index(index))
            self._heapify_up(self._parent_index(index))

    def _swap_elements(self, i1: int, i2: int):
        self.array[i1], self.array[i2] = self.array[i2], self.array[i1]

    def poll(self):
        return self.poll_object()["item"]

    def poll_object(self):
        top = self.array[1].copy()
        # Swap values of first and last elements
        self._swap_elements(1, len(self.array) - 1)
        self.array.pop(len(self.array) - 1)

        self._heapify_down(1)
        return top

    def _heapify_down(self, index: int):
        if self._is_leaf(index):
            return  # Don't swap if left index is empty
        elif self.array[index]["priority"] > self.get_left_child(index)["priority"]:
            self._swap_elements(index, self._left_index(index))
            self._heapify_down(self._left_index(index))

        else:
            if not self._is_contained(self._right_index(index)):
                return  # Don't swap if right index is empty
            elif self.array[index]["priority"] > self.get_right_child(index)["priority"]:
                self._swap_elements(index, self._right_index(index))
                self._heapify_down(self._right_index(index))

    def _is_leaf(self, index: int) -> bool:
        return not (self._is_contained(self._left_index(index))
                    or self._is_contained(self._right_index(index)))

    def _is_contained(self, index: int) -> bool:
        return index < self.size

    @staticmethod
    def _parent_index(index: int) -> int:
        return math.floor(index / 2)

    @staticmethod
    def _left_index(index: int) -> int:
        return 2 * index

    @staticmethod
    def _right_index(index: int) -> int:
        return 2 * index + 1

    def get_parent(self, index: int):
        return self.array[self._parent_index(index)]

    def get_children(self, index: int):
        return [self.get_left_child(index), self.get_right_child(index)]

    def get_left_child(self, index: int):
        return self.array[2 * index]

    def get_right_child(self, index: int):
        return self.array[2 * index + 1]

    def get_sort(self):
        pq = PriorityQueue()
        for _ in range(self._OFFSET, len(self.array), 1):
            # Swap values of first and last elements
            self._swap_elements(1, len(self.array) - 1)
            self._heapify_down(1)
            item = self.array.pop(1)
            pq.enqueue(item["item"], item["priority"])
        return pq

    def peek(self):
        if not self.size == 0:
            return self.array[self._OFFSET]
        else:
            raise IndexError("Heap is empty.")

    def back(self):
        if not self.size == 0:
            return self.array[len(self.array) - 1]
        else:
            raise IndexError("Heap is empty.")

    def print(self):
        i = 0
        lower_bound = 0
        upper_bound = 1

        while upper_bound <= (len(self.array) + 2 ** i):
            # Recalculate upper bound if last row is not full
            if len(self.array) - self._OFFSET < upper_bound:
                upper_bound = len(self.array) - self._OFFSET

            for j in range(lower_bound + self._OFFSET, upper_bound + self._OFFSET):
                print(self.array[j]["priority"], end=" ")
            print()

            i += 1
            lower_bound = 2 ** i - 1
            upper_bound = 2 ** (i + 1) - 1


# heap = MinHeap([["d", 5], ["e", 4], ["a", 3], ["c", 2], ["b", 1]])
# heap.append("d", 5)
# heap.append("e", 4)
# heap.append("a", 3)
# heap.append("c", 2)
# heap.append("b", 1)
# heap.get_sort().print_elements()


