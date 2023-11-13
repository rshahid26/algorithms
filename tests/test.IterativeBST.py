from data_structures import IterativeBST

bst_list = [14, 3, 22, 1, 7, 17, 30]
bst = IterativeBST()
for i in bst_list:
    bst.append(i)

bst.append(0)
bst.append(31)
bst.delete(31)
bst.print()

print()
print("Inorder:", bst.in_order())
print("Preorder:", bst.pre_order())
print("Postorder:", bst.post_order())

