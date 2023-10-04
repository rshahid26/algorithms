from data_structures import RecursiveBST

bst_list = [14, 3, 22, 1, 7, 17, 30]
bst = RecursiveBST()
for i in bst_list:
    bst.append(i)

print(bst.in_order())
print(bst.root.left.left.parent.parent.data)

