import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, id_):
        self.id = id_
        self.predecessors = set()
        self.successors = set()


class Graph:
    def __init__(self, weight_func, symetric=True, path=None):
        self.symetric = symetric
        self.src = None
        self.dest = None
        self.nodes = {}
        self.edges = {}
        self.get_weight = weight_func

        if path:
            with open(path) as data:
                self.import_data(data)

    def add_node(self, id_, src=False, dest=False):
        node = Node(id_)
        self.nodes[id_] = node

        if src:
            self.src = node
        if dest:
            self.dest = dest

    def add_edge(self, id_1, id_2, lat, risk):
        if id_1 not in self.nodes.keys():
            self.add_node(id_1)
        if id_2 not in self.nodes.keys():
            self.add_node(id_2)

        self.edges[(id_1, id_2)] = (lat, risk)
        self.nodes[id_1].successors.add(self.nodes[id_2])
        self.nodes[id_2].predecessors.add(self.nodes[id_1])
        if self.symetric:
            # self.edges[(id_2, id_2)] = (lat, risk) # might need later
            self.nodes[id_2].successors.add(self.nodes[id_1])
            self.nodes[id_1].predecessors.add(self.nodes[id_2])

    def import_data(self, data):
        """
        data structure:
        0 or 1                          # 1 if symetric, 0 if not
        src_node
        dest_node
        node1,node2,latency,risk        # edges
        """
        self.symetric = next(data)[:-1] == "1"
        self.add_node(next(data)[:-1], src=True)
        self.add_node(next(data)[:-1], src=False)
        for line in data:
            n1, n2, lat, risk = line.split(sep=",")
            self.add_edge(n1, n2, float(lat), float(risk))

    def visualize(self):
        self.vis = nx.Graph() if self.symetric else nx.DiGraph()
        nodes = [n.id for n in self.nodes.values()]
        edges = [(*k, self.get_weight(*v)) for k, v in self.edges.items()]
        print(nodes)
        print(edges)
        self.vis.add_nodes_from(nodes)
        self.vis.add_weighted_edges_from(edges)
        nx.draw(self.vis, with_labels=True)
        plt.show()
