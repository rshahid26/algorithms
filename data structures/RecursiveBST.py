class Node:
    def __init__(self, data=None, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right


class RecursiveBST:
    def __init__(self, data=None):
        self.root = Node(data)

    def find_node(self, data, node=None):
        """Returns a reference to the node with the given data"""
        if node is None:
            node = self.root

        if node.data == data:
            return node
        elif data > node.data:
            return self.find_node(data, node.right)
        else:
            return self.find_node(data, node.left)

    def append(self, data, node=None, parent=None):
        if node is None:
            node = self.root

        if node.data is None:
            node.data = data
            return node

        if data > node.data:
            if node.right is None:
                node.right = Node(data, parent)
                return node.right
            else:
                return self.append(data, node.right, node)
        else:
            if node.left is None:
                node.left = Node(data, parent)
                return node.left
            else:
                return self.append(data, node.left, node)


bst = RecursiveBST()
bst.append(14)
bst.append(3)
bst.append(22)
print(bst.root.left.data)
print(bst.find_node(3).data)
