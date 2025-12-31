class Node:
    def __init__(self, id_):
        self.id = id_
        self.predecessors = set()
        self.successors = set()
