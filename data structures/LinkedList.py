class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList:
    count = 0

    def __init__(self, data):
        self.head = Node(data)
        LinkedList.count += 1

    def append(self, data):
        current = self.head

        while current.next is not None:
            current = current.next

        current.next = Node(data)

    def prepend(self, data):
        head = Node(data)
        head.next = self.head

        self.head = head

    def remove(self, target_data):
        while self.head.data == target_data:
            self.head = self.head.next

        current = self.head
        while current.next is not None:
            if current.next.data == target_data:
                current.next = current.next.next

            else:
                current = current.next

    def print(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

    @staticmethod
    def get_count():
        print(LinkedList.count)