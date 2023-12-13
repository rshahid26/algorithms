from .RecursiveBST import RecursiveBST, Node
class AVLNode(Node):
    def __init__(self, val=None, left=None, right=None, parent=None):
        super().__init__(val, left, right)
        self.parent = parent
        self.height = 0

    def bf(self):
        return AVLTree.height(self.right) - AVLTree.height(self.left)


class AVLTree(RecursiveBST):
    def __init__(self, val=None):
        self.MAX_IMBALANCE = 1
        self.root = Node(val)

    @staticmethod
    def height(node: AVLNode):
        return -1 if node is None else node.height

    def append(self, val) -> None:
        """Inserts a new node with given val into the binary tree in O(logn) time."""
        if self.root is None or self.root.val is None:
            self.root = AVLNode(val)
        else:
            self._append_recursive(self.root, val)

    def _append_recursive(self, node: AVLNode, val):
        if node is None:
            return AVLNode(val)

        if val < node.val:
            node.left = self._append_recursive(node.left, val)
            node.left.parent = node
        elif val > node.val:
            node.right = self._append_recursive(node.right, val)
            node.right.parent = node
        else:
            raise Exception("nodes must have unique values.")

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        return self.balance(node)

    def delete(self, val):
        """Deletes a node with the given val from the tree in O(logn) time."""
        self.root = self._delete_recursive(self.root, val)

    def _delete_recursive(self, node, val):
        node = super()._delete_recursive(node, val)
        if node is not None:
            node.height = 1 + max(self.height(node.left), self.height(node.right))
            return self.balance(node)

    def balance(self, node: AVLNode):
        # Right subtree is too long
        if node.bf() > self.MAX_IMBALANCE:
            # Right subtree leans right.
            if node.right.bf() >= 0:
                return self.rotate_left(node)
            # Right subtree leans left. Rotate the right subtree to lean right first.
            else:
                self.rotate_right(node.right)
                return self.rotate_left(node)

        # Left subtree is too long
        if node.bf() < -self.MAX_IMBALANCE:
            # Left subtree leans left.
            if node.left.bf() <= 0:
                return self.rotate_right(node)
            # Left subtree leans right. Rotate the left subtree to lean left first.
            else:
                self.rotate_left(node.left)
                return self.rotate_right(node)
        return node

    def rotate_left(self, node: AVLNode):
        #   Before:    |      After:        |  x,y, and z necessarily exist to trigger rotate_left.
        #      x       |        y           |
        #       \      |       / \          |  temp may or may not exist. this is only relevant when
        #        y     |      x   z         |  setting temp's parent to x.
        #       / \    |       \            |
        #   temp   z   |      temp          |  note that z and y.right is unchanged.

        x, y = node, node.right

        temp = y.left
        y.left = x
        x.right = temp

        y.parent = x.parent
        x.parent = y
        if temp:
            temp.parent = x

        if y.parent is None: # x was a root
            self.root = y

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def rotate_right(self, node: AVLNode):
        #   Before:    |      After:        |  x, y, and z necessarily exist to trigger rotate_right.
        #      x       |        y           |
        #     /        |       / \          |  temp may or may not exist. this is only relevant when
        #    y         |      z   x         |  setting temp's parent to x.
        #   / \        |         /          |
        #  z   temp    |        temp        |  note that z and y.left is unchanged.

        x, y = node, node.left

        temp = y.right
        y.right = x
        x.left = temp

        y.parent = x.parent
        x.parent = y
        if temp:
            temp.parent = x

        if y.parent is None: # x was a root
            self.root = y

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y