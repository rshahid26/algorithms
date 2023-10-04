from data_structures import BinarySearchTree

bst_list = [14, 3, 22, 1, 7, 17, 30]
bst = BinarySearchTree()
for i in bst_list:
    bst.append(i)

bst.append(0)
bst.print_tree()
print("Inorder", bst.in_order())
print("Preorder", bst.pre_order())
print("Postorder", bst.post_order())

