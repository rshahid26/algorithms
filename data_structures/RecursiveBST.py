class Node:
    """Represents a node in a binary tree."""

    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RecursiveBST:
    """A binary search tree with recursive methods."""

    def __init__(self, val=None):
        self.root = Node(val)

    def append(self, val) -> None:
        """Inserts a new node with given val into the binary tree in O(logn) time."""
        if self.root is None or self.root.val is None:
            self.root = Node(val)
        else:
            self._append_recursive(self.root, val)

    def _append_recursive(self, node, val):
        if node is None:
            return Node(val)

        if val < node.val:
            node.left = self._append_recursive(node.left, val)
        elif val > node.val:
            node.right = self._append_recursive(node.right, val)
        else:
            raise Exception("nodes must have unique values.")
        return node

    def find_node(self, val):
        """Returns a reference to the node with the given val in O(logn) time."""
        return self._find_node_recursive(self.root, val)

    def _find_node_recursive(self, node, val):
        if node is None or node.val == val:
            return node

        if val < node.val:
            return self._find_node_recursive(node.left, val)
        else:
            return self._find_node_recursive(node.right, val)

    def delete(self, val):
        """Deletes a node with the given val from the tree in O(logn) time."""
        self.root = self._delete_recursive(self.root, val)

    def _delete_recursive(self, node, val):
        if node is None:
            return node

        if val < node.val:
            node.left = self._delete_recursive(node.left, val)
        elif val > node.val:
            node.right = self._delete_recursive(node.right, val)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._recursive_get_min(node.right)
            node.val = temp.val
            node.right = self._delete_recursive(node.right, temp.val)
        return node

    def get_successor(self, node):
        """Finds the in-order successor of a given node in the tree in O(logn) time."""
        if node is None or node.val is None:
            return None
        return self._get_successor_recursive(node.right)

    def _get_successor_recursive(self, node):
        if node.left is None:
            return node.val
        else:
            return self._get_successor_recursive(node.left)

    def get_predecessor(self, node):
        """Finds the in-order predecessor of a given node in the tree in O(logn) time."""
        if node is None or node.val is None:
            return None
        return self._get_predecessor_recursive(node.left)

    def _get_predecessor_recursive(self, node):
        if node.right is None:
            return node.val
        else:
            return self._get_predecessor_recursive(node.right)

    def get_min(self):
        return self._recursive_get_min(self.root)

    def _recursive_get_min(self, node):
        if node.left is None:
            return node.val
        else:
            return self._recursive_get_min(node.left)

    def get_max(self):
        return self._recursive_get_max(self.root)

    def _recursive_get_max(self, node):
        if node.right is None:
            return node.val
        else:
            return self._recursive_get_max(node.right)

    def in_order(self, node: Node = None, result: list = None):
        if result is None:
            result = []
            node = self.root if node is None else node

        if node is not None:
            self.in_order(node.left, result)
            result.append(node.val)
            self.in_order(node.right, result)
        return result

    def pre_order(self, node: Node = None, result: list = None):
        if result is None:
            result = []
            node = self.root if node is None else node

        if node is not None:
            result.append(node.val)
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
            result.append(node.val)
        return result

    def validate(self):
        return self._validate_recursive(self, self.root)
    def _validate_recursive(self, node, low=-float('inf'), high=float('inf')):
        if not node:
            return True
        if not (low < node.val < high):
            return False

        valid_left = self._validate_recursive(node.left, low, node.val)
        valid_right = self._validate_recursive(node.right, node.val, high)

        return valid_left and valid_right

    def print(self, node=None, level=0, prefix="C: "):
        """Recursive function to print the tree."""
        if node is None:
            node = self.root

        print(" " * (level * 4) + prefix + str(node.val))
        if node.left is not None or node.right is not None:
            if node.left is not None:
                self.print(node.left, level + 1, "L: ")
            else:
                print(" " * ((level + 1) * 4) + "L: ")

            if node.right is not None:
                self.print(node.right, level + 1, "R: ")
            else:
                print(" " * ((level + 1) * 4) + "R: ")