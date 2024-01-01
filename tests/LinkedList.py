from data_structures import LinkedList

l = LinkedList([2, 3, 5, 5, 3, 5, 1])
l.print()
l.remove_value(2)
print("Remove 2, head is now", l.head.val)
l.remove_index(l.length - 1)
print("Remove tail, tail is now", l.get_index(l.length - 1))
l.prepend(1)
print("Prepend 1, head is now", l.head.val)
l.print()
l.remove_value(5, 2)
print("Remove first two 5's, list is now")
l.print()