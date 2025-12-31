import networkx as nx
import matplotlib.pyplot as plt

from helpers import comb_gen
from . import Node


class Graph:
    def __init__(self, symetric=True, path=None):
        self.symetric = symetric
        self.src = None
        self.dest = None
        self.nodes = {}
        self.edges = {}

        if path:
            with open(path) as data:
                self.import_data(data)

    def add_node(self, id_, src=False, dest=False):
        node = Node(id_)

        if id_ not in self.nodes:
            self.nodes[id_] = node

        if src:
            self.src = node
        if dest:
            self.dest = node

    def add_edge(self, id_1, id_2, lat, risk):
        if id_1 not in self.nodes.keys():
            self.add_node(id_1)
        if id_2 not in self.nodes.keys():
            self.add_node(id_2)

        self.edges[(id_1, id_2)] = (lat, risk)
        self.nodes[id_1].successors.add(self.nodes[id_2])
        self.nodes[id_2].predecessors.add(self.nodes[id_1])
        if self.symetric:
            self.edges[(id_2, id_1)] = (lat, risk)
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
        self.add_node(next(data)[:-1], dest=True)
        for line in data:
            n1, n2, lat, risk = line.split(sep=",")
            self.add_edge(n1, n2, float(lat), float(risk))

    def get_layered_pos(self):
        if self.src is None:
            return nx.spring_layout(self.vis)

        pos = {}
        layers = {}
        visited = set()

        queue = [(self.src, 0)]
        visited.add(self.src.id)

        while queue:
            current_node, depth = queue.pop(0)

            if depth not in layers:
                layers[depth] = []
            layers[depth].append(current_node.id)

            sorted_successors = sorted(
                list(current_node.successors), key=lambda x: x.id
            )

            for neighbor in sorted_successors:
                if neighbor.id not in visited:
                    visited.add(neighbor.id)
                    queue.append((neighbor, depth + 1))

        for depth, node_ids in layers.items():
            for i, node_id in enumerate(node_ids):
                y = (len(node_ids) - 1) / 2 - i
                pos[node_id] = (depth, y)

        detached = [n for n in self.nodes if n not in visited]
        for i, node_id in enumerate(detached):
            y = (len(detached) - 1) / 2 - i
            pos[node_id] = (-1 / 2, y / 2)

        return pos

    def visualize(self, weight_func=None, block=True):
        if weight_func is None:
            weight_func = comb_gen(1, 1)

            def label_func(x, y):
                return str((x, y))
        else:

            def label_func(x, y):
                return str(weight_func(x, y))

        self.vis = nx.Graph() if self.symetric else nx.DiGraph()

        nodes = [n.id for n in self.nodes.values()]
        edges = [(*k, weight_func(*v)) for k, v in self.edges.items()]
        labels = {k: label_func(*v) for k, v in self.edges.items()}

        self.vis.add_nodes_from(nodes)
        self.vis.add_weighted_edges_from(edges)

        pos = self.get_layered_pos()

        nx.draw(
            self.vis,
            pos=pos,
            with_labels=True,
            node_color="cyan",
            node_size=800,
            font_weight="bold",
        )
        nx.draw_networkx_edge_labels(
            self.vis, pos=pos, edge_labels=labels, label_pos=0.3
        )

        plt.show(block=block)
