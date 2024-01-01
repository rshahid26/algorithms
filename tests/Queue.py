from data_structures import Queue

q1 = Queue(4)
q1.print()
q2 = Queue([4, 5, 6, 2, 7, 4])
q2.print()
while q2.length:
    print(q2.popleft())

q2.append(9)
print(q2.peek())