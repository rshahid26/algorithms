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
            return

        def _append(node, val):
            if node is None:
                return Node(val)
            if val < node.val:
                node.left = _append(node.left, val)
            elif val > node.val:
                node.right = _append(node.right, val)
            else:
                raise Exception("nodes must have unique values.")
            return node

        _append(self.root, val)

    def find_node(self, val):
        """Returns a reference to the node with the given val in O(logn) time."""
        def _find_node(node, val):
            if node is None or node.val == val:
                return node
            if val < node.val:
                return _find_node(node.left, val)
            else:
                return _find_node(node.right, val)

        return _find_node(self.root, val)

    def delete(self, val):
        """Deletes a node with the given val from the tree in O(logn) time."""
        def _delete(node, val):
            if node is None:
                return node
            if val < node.val:
                node.left = _delete(node.left, val)
            elif val > node.val:
                node.right = _delete(node.right, val)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                temp = self._get_min(node.right)
                node.val = temp.val
                node.right = _delete(node.right, temp.val)
            return node

        _delete(self.root, val)

    def get_successor(self, node):
        """Finds the in-order successor of a given node in the tree in O(logn) time."""
        if node is None or node.val is None:
            return None

        def _get_successor(node):
            if node.left is None:
                return node.val
            else:
                return _get_successor(node.left)

        return _get_successor(node.right)

    def get_predecessor(self, node):
        """Finds the in-order predecessor of a given node in the tree in O(logn) time."""
        if node is None or node.val is None:
            return None

        def _get_predecessor(node):
            if node.right is None:
                return node.val
            else:
                return _get_predecessor(node.right)

        return _get_predecessor(node.left)

    def get_min(self):
        def _get_min(node):
            if node.left is None:
                return node
            else:
                return _get_min(node.left)

        return _get_min(self.root).val

    def get_max(self):
        def _get_max(node):
            if node.right is None:
                return node
            else:
                return _get_max(node.right)

        return _get_max(self.root).val

    def in_order(self, node: Node = None, result: list = None):
        if result is None:
            result = []
            node = self.root if node is None else node

        def _in_order(node):
            if node is not None:
                _in_order(node.left)
                result.append(node.val)
                _in_order(node.right)

        _in_order(node)
        return result

    def pre_order(self, node: Node = None, result: list = None):
        if result is None:
            result = []
            node = self.root if node is None else node

        def _pre_order(node):
            if node is not None:
                result.append(node.val)
                _pre_order(node.left)
                _pre_order(node.right)

        _pre_order(node)
        return result

    def post_order(self, node: Node = None, result: list = None):
        if result is None:
            result = []
            node = self.root if node is None else node

        def _post_order(node):
            if node is not None:
                _post_order(node.left)
                _post_order(node.right)
                result.append(node.val)

        _post_order(node)
        return result

    def validate(self):
        def _validate(node, low=-float('inf'), high=float('inf')):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return _validate(node.left, low, node.val) and _validate(node.right, node.val, high)

        return _validate(self.root)

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
