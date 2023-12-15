from algorithms.sorting import quicksort
from data_structures.AVLTree import AVLTree


nodes = [0, 14, 3, 22, 1, 7, 17, 30]
avl_list = quicksort(nodes)
print(avl_list)

avl = AVLTree()
for idx, i in enumerate(avl_list):
    avl.append(i)
    print("appended", avl_list[idx])
    avl.print()
    print()

print("deleting node", 14)
avl.delete(14)
avl.print()

print("deleting node", 22)
avl.delete(22)
avl.print()

print("deleting root node", avl.root.val)
avl.delete(avl.root.val)
avl.print()

print("inorder:", avl.in_order())
print("preorder:", avl.pre_order())
print("postorder:", avl.post_order())

print("successor of", avl.root.val, "is", avl.get_successor(avl.root))
print("predecessor of", avl.root.val, "is", avl.get_predecessor(avl.root))
