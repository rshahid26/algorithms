class Node:
    """Represents a node in a binary tree."""
    size = 0

    def __init__(self, data=None, parent=None, right=None, left=None):
        self.data = data
        self.parent = parent
        self.right = right
        self.left = left


class BinarySearchTree:
    """A binary search tree with non-recursive methods."""

    def __init__(self, data=None):
        self.root = Node(data)

    def append(self, data) -> None:
        """Inserts a new node with given data into the binary tree."""
        if self.root.data is None:
            self.root.data = data
            return

        current = self.root
        while True:
            if data > current.data:
                if current.right is None:
                    current.right = Node(data, current)
                    return
                current = current.right
            else:
                if current.left is None:
                    current.left = Node(data, current)
                    return
                current = current.left

    def find_node(self, data):
        current = self.root
        while current is not None:
            if current.data == data:
                return current

            if data > current.data:
                current = current.right
            else:
                current = current.left
        return None

    def delete(self, data):
        """Deletes a node with the given data from the binary tree"""
        to_delete = self.find_node(data)
        if to_delete is None:
            return
        elif to_delete == self.root:
            self._delete_root()

        else:
            num_children = sum((to_delete.left is not None, to_delete.right is not None))
            if num_children == 0:
                self.replace_node(to_delete)
            elif num_children == 1:
                self.replace_node(to_delete, to_delete.left or to_delete.right)
            elif num_children == 2:
                successor = self.get_successor(to_delete)
                to_delete.data = successor.data
                self.replace_node(successor, successor.right)

    def _delete_root(self):
        """Deletes the root node from the binary tree"""
        num_children = sum((self.root.left is not None, self.root.right is not None))
        if num_children == 0:
            self.root = None
        elif num_children == 1:
            self.root = self.root.left or self.root.right
        elif num_children == 2:
            successor = self.get_successor(self.root)
            self.root.data = successor.data
            self.replace_node(successor, successor.right)

    def replace_node(self, child: Node, new_child: Node = None) -> None:
        """Replaces the child node with the new_child node in the tree"""
        if new_child:
            new_child.parent = child.parent
        if child == self.root:
            self.root = new_child

        elif child.parent.left == child:
            child.parent.left = new_child
        elif child.parent.right == child:
            child.parent.right = new_child

    def get_successor(self, node: Node) -> Node:
        """Finds the in-order successor of a given node in the tree"""
        if node.right is None:
            ancestor = node.parent
            while ancestor is not None and node == ancestor.right:
                node, ancestor = ancestor, ancestor.parent
            return ancestor

        else:
            successor = node.right
            while successor.left is not None:
                successor = successor.left
            return successor

    def get_predecessor(self, node):
        """Finds the in-order predecessor of a given node in the tree"""
        if node.left is None:
            ancestor = node.parent
            while ancestor is not None and node == ancestor.left:
                node, ancestor = ancestor, ancestor.parent
            return ancestor

        else:
            successor = node.left
            while successor.right is not None:
                successor = successor.right
            return successor

    def _get_sort(self):
        left_most = []

        current = self._get_min_node()
        while current is not None:
            left_most.append(current.data)
            current = self.get_successor(current)

        return left_most

    def in_order(self):
        order = []
        stack = []
        current = self.root

        while stack or current:  # "or current" for when left subtree is exhausted
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                order.append(current.data)
                current = current.right
        return order

    def pre_order(self):
        stack = [self.root] if self.root is not None else []
        order = []

        while stack:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            order.append(current.data)
        return order

    def post_order(self):
        stack = [self.root] if self.root is not None else []
        order = []

        while stack:
            current = stack.pop()
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
            order.append(current.data)
        order.reverse()
        return order

    def get_min(self):
        return self._get_min_node().data

    def _get_min_node(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current

    def get_max(self):
        return self._get_max_node().data

    def _get_max_node(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current

    def print_tree(self, node=None, level=0, prefix="C: "):
        """Recursive function to print the tree."""
        if node is None:
            node = self.root

        print(" " * (level * 4) + prefix + str(node.data))
        if node.left is not None or node.right is not None:
            if node.left is not None:
                self.print_tree(node.left, level + 1, "L: ")
            else:
                print(" " * ((level + 1) * 4) + "L: ")

            if node.right is not None:
                self.print_tree(node.right, level + 1, "R: ")
            else:
                print(" " * ((level + 1) * 4) + "R: ")