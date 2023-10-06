class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


class LinkedList:
    def __init__(self, values=None):
        if values is None:
            self.head = None
            self._length = 0
        elif type(values) == list:
            self.head = Node(values[0])
            self._length = 1
            for i in range(1, len(values)):
                self.append(values[i])
        else:
            self.head = Node(values)
            self._length = 1

    @property
    def length(self):
        return self._length
    
    def append(self, val) -> None:
        if self.head is None:
            self.head = Node(val)
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = Node(val)
        self._length += 1
        
    def prepend(self, val):
        head = Node(val)
        head.next = self.head
        
        self.head = head
        self._length += 1

    def remove_value(self, target, times: int = None) -> None:
        if self.head is None or times is not None and times <= 0:
            return

        while self.head.val == target:
            self.head = self.head.next
            self._length -= 1

        current = self.head
        while current.next is not None:
            if current.next.val == target:
                current.next = current.next.next
                self._length -= 1

                if times is not None:
                    times -= 1
                    if times == 0:
                        return
            else:
                current = current.next

    def get_index(self, index):
        if self.head is None or index < 0 or index >= self._length:
            return None

        current = self.head
        current_index = 0
        while current_index != index:
            current = current.next
            current_index += 1
        return current.val

    def remove_index(self, index):
        if self.head is None or index < 0 or index >= self._length:
            return None

        self._length -= 1
        if index == 0:
            removed_value = self.head.val
            self.head = self.head.next
            return removed_value

        current = self.head
        current_index = 0
        while current_index != index - 1:
            current = current.next
            current_index += 1
            
        removed = current.next.val
        current.next = current.next.next
        return removed
            
    def print(self) -> None:
        current = self.head

        while current is not None:
            print(current.val, end=" ")
            current = current.next
        print()
        