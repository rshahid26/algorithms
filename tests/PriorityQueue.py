from data_structures import PriorityQueue

pq = PriorityQueue()
pq.append("B", 2)
pq.append("D", 3)
pq.append("C", 3)
pq.append("D", 4)
pq.append("A", 1)


pq.print_elements()
print("elements:")
pq.print_elements()
print("priorities:")
print(pq.list_priorities())
while pq.length:
    print(pq.popleft())
