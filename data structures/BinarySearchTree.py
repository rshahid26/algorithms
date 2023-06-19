class Node:
    """Represents a node in a binary tree."""

    def __init__(self, data=None, parent=None, right=None, left=None):
        self.data = data
        self.parent = parent
        self.right = right
        self.left = left


# noinspection PyMethodMayBeStatic
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
        """Returns a reference to the node with the given data."""
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
        successor = node.right
        while successor.left is not None:
            successor = successor.left

        return successor

    def get_predecessor(self, node):
        """Finds the in-order predecessor of a given node in the tree"""
        successor = node.left
        while successor.right is not None:
            successor = successor.right

        return successor

    def inorder_traversal(self):
        """Performs an in-order traversal of the tree."""
        current = self.root
        stack = []

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.data, end=" ")
                current = current.right
            else:
                break

    def preorder_traversal(self):
        """Performs a pre-order traversal of the tree."""
        current = self.root
        stack = []

        while True:
            if current is not None:
                print(current.data, end=" ")
                if current.right is not None:
                    stack.append(current.right)
                current = current.left
            elif stack:
                current = stack.pop()
            else:
                break

    def postorder_traversal(self):
        """Performs a post-order traversal of the tree."""
        stack1 = [self.root]
        stack2 = []

        while stack1:
            current = stack1.pop()
            stack2.append(current)

            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)

        while stack2:
            current = stack2.pop()
            print(current.data, end=" ")

    def get_min(self):
        current = self.root
        while current.left is not None:
            current = current.left

        return current.data

    def get_max(self):
        current = self.root
        while current.right is not None:
            current = current.right

        return current.data


bst_list = [14, 3, 22, 1, 7, 17, 30]
bst = BinarySearchTree()
for i in bst_list:
    bst.append(i)

print(bst.postorder_traversal())
bst.delete(22)
print(bst.postorder_traversal())
