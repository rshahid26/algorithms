class Node:
    """Represents a node in a binary tree."""

    def __init__(self, data=None, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right


class RecursiveBST:
    """A binary search tree with recursive methods."""

    def __init__(self, data=None):
        self.root = Node(data)

    def append(self, data) -> None:
        """Inserts a new node with given data into the binary tree in O(logn) time."""
        if self.root is None or self.root.data is None:
            self.root = Node(data)
        else:
            self._append_recursive(self.root, data)

    def _append_recursive(self, node, data):
        if node is None:
            return Node(data)

        if data < node.data:
            node.left = self._append_recursive(node.left, data)
            node.left.parent = node
        elif data > node.data:
            node.right = self._append_recursive(node.right, data)
            node.right.parent = node

        return node

    def find_node(self, data):
        """Returns a reference to the node with the given data in O(logn) time."""
        return self._find_node_recursive(self.root, data)

    def _find_node_recursive(self, node, data):
        if node is None or node.data == data:
            return node

        if data < node.data:
            return self._find_node_recursive(node.left, data)
        else:
            return self._find_node_recursive(node.right, data)

    def delete(self, data):
        """Deletes a node with the given data from the tree in O(logn) time."""
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, node, data):
        if node is None:
            return node

        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._recursive_get_min(node.right)
            node.data = temp.data
            node.right = self._delete_recursive(node.right, temp.data)
        return node

    def get_successor(self, node):
        """Finds the in-order successor of a given node in the tree in O(logn) time."""
        if node is None or node.data is None or node.right is None:
            return None
        else:
            return self._get_successor_recursive(node.right)

    def _get_successor_recursive(self, node):
        if node.left is None:
            return node.data
        else:
            return self._get_successor_recursive(node.left)

    def get_predecessor(self, node):
        """Finds the in-order predecessor of a given node in the tree in O(logn) time."""
        if node is None or node.data is None or node.left is None:
            return None
        else:
            return self._get_predecessor_recursive(node.left)

    def _get_predecessor_recursive(self, node):
        if node.right is None:
            return node.data
        else:
            return self._get_predecessor_recursive(node.right)

    def get_min(self):
        return self._recursive_get_min(self.root)

    def _recursive_get_min(self, node):
        if node.left is None:
            return node.data
        else:
            return self._recursive_get_min(node.left)

    def get_max(self):
        return self._recursive_get_max(self.root)

    def _recursive_get_max(self, node):
        if node.right is None:
            return node.data
        else:
            return self._recursive_get_max(node.right)

    def in_order(self, node: Node = None, result: list = None):
        if result is None:
            result = []
            node = self.root if node is None else node

        if node is not None:
            self.in_order(node.left, result)
            result.append(node.data)
            self.in_order(node.right, result)
        return result

    def pre_order(self, node: Node = None, result: list = None):
        if result is None:
            result = []
            node = self.root if node is None else node

        if node is not None:
            result.append(node.data)
            self.pre_order(node.left, result)
            self.pre_order(node.right, result)
        return result

    def post_order(self, node: Node = None, result: list = None):
        if result is None:
            result = []
            node = self.root if node is None else node

        if node is not None:
            self.post_order(node.left, result)
            self.post_order(node.right, result)
            result.append(node.data)
        return result
