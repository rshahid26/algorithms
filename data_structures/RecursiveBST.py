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

    def in_order_traversal(self):
        result = []
        self._in_order_traversal_recursive(self.root, result)
        return result

    def _in_order_traversal_recursive(self, node, result):
        if node is not None:
            self._in_order_traversal_recursive(node.left, result)
            result.append(node.data)
            self._in_order_traversal_recursive(node.right, result)

    def pre_order_traversal(self):
        """Wrapper for the recursive pre-order traversal method in O(n) time."""
        result = []
        self._pre_order_traversal_recursive(self.root, result)
        return result

    def _pre_order_traversal_recursive(self, node, result):
        if node is not None:
            result.append(node.data)
            self._pre_order_traversal_recursive(node.left, result)
            self._pre_order_traversal_recursive(node.right, result)

    def post_order_traversal(self):
        """Wrapper for the recursive post-order traversal method in O(n) time."""
        result = []
        self._post_order_traversal_recursive(self.root, result)
        return result

    def _post_order_traversal_recursive(self, node, result):
        if node is not None:
            self._post_order_traversal_recursive(node.left, result)
            self._post_order_traversal_recursive(node.right, result)
            result.append(node.data)


bst_list = [14, 3, 22, 1, 7, 17, 30]
bst = RecursiveBST()
for i in bst_list:
    bst.append(i)

print(bst.in_order_traversal())
print(bst.root.left.left.parent.parent.data)


