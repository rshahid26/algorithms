from data_structures import RecursiveBST

bst_list = [14, 3, 22, 1, 7, 17, 30]
bst = RecursiveBST()
for i in bst_list:
    bst.append(i)

bst.print()
print("inorder:", bst.in_order())
print("preorder:", bst.pre_order())
print("postorder:", bst.post_order())

print()
print("successor of", bst.root.val, "is", bst.get_successor(bst.root))
print("predecessor of", bst.root.val, "is", bst.get_predecessor(bst.root))


