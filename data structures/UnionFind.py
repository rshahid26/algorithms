class UnionFind:
    def __init__(self, elements: list = None):
        self.map = {}
        self.parents = []

        for i, element in enumerate(elements):
            self.map[element] = i
            self.parents.append(i)

    def union(self, e1, e2):
        e1_root, e1_rank = self.find(self.map[e1])
        e2_root, e2_rank = self.find(self.map[e2])

        if e1_root == e2_root:
            return
        elif e1_rank <= e2_rank:
            self.parents[e1_root] = e2_root
        else:
            self.parents[e2_root] = e1_root

    def find(self, element) -> int:
        index = self.map[element]
        root, _ = self._root_info(index)
        return root

    def is_connected(self, e1, e2) -> bool:
        return self.find(e1) == self.find(e2)

    def rank(self, element) -> int:
        index = self.map[element]
        _, rank = self._root_info(index)
        return rank

    def _root_info(self, index, rank=0) -> tuple:
        if self.parents[index] == index:
            return index, rank
        else:
            rank += 1
            root, rank = self._root_info(self.parents[index], rank)
            self.parents[index] = root
            return root, rank

    def num_partitions(self):
        history = {}
        count = 0

        for root in self.parents:
            if root not in history:
                count += 1
                history[root] = True
        return count


u = UnionFind(["a", "b", "c", "d", "e", "f"])
u.union("a", "b")
u.union("c", "d")
u.union("b", "c")
print(u.parents)
print(u.num_partitions())

