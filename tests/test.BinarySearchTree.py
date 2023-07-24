from data_structures import BinarySearchTree

bst_list = [14, 3, 22, 1, 7, 17, 30]
bst = BinarySearchTree()
for i in bst_list:
    bst.append(i)

bst.append(0)
print(bst.preorder_traversal())
print(bst.inorder_traversal())
print(bst.postorder_traversal())
