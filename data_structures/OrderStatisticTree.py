from .AVLTree import AVLNode, AVLTree


class OSNode(AVLNode):
    def __init__(self, val=None, left=None, right=None, parent=None):
        super().__init__(val, left, right, parent)
        self.size = 1


class OSTree(AVLTree):
    """A balanced BST that can retrieve order statistics in O(logn) time."""
    def __init__(self, val=None):
        self.MAX_IMBALANCE = 1
        self.root = OSNode(val)
    
    def __init__(self, val=None):
        self.MAX_IMBALANCE = 1
        self.root = OSNode(val)
    
    def append(self, val) -> None:
        if self.root is None or self.root.val is None:
            self.root = OSNode(val)
            return
        
        super().append(val)
        self._update_size(self.root, val)
        
    def delete(self, val) -> None:
        super().delete(val)
        self._update_size(self.root, val)
    
    def _update_size(self, node, val):
        if node is None:
            return
        node.size += 1
        if val == node.val:
            return
        if val < node.val:
            self._update_size(node.left, val)
        elif val > node.val:
            self._update_size(node.right, val)
    
    def get_os(self, k):
        """Returns the 1-indexed kth order statistic in the tree."""
        if k < 1 or k > self.root.size:
            raise ValueError("k is not a valid 1-indexed order statistic.")
        
        def _get_os(node: AVLNode, k: int):
            sub_os = AVLTree.height(node.left) + 1
            if k == sub_os:
                return node.val
            elif k < sub_os:
                return _get_os(node.left, k)
            else:
                return _get_os(node.right, k - sub_os)

        return _get_os(self.root, k)