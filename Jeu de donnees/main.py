import networkx as nx
import matplotlib.pyplot as plt

class graph:
    def __init__(self,nodes_table:list=None,weighted_edges_table:list=None,nodes_positions:dict={},symetric=True):
        try :
            self.nodes_table=list(dict.fromkeys(nodes_table))
        except:
            self.nodes_table=nodes_table
        self.weighted_edges_table=weighted_edges_table
        self.nodes_positions=nodes_positions
        self.source_found=0
        self.destination_found=0
        self.graph=None
        self.symetric=symetric

    def add_node(self,node,is_source=False,is_destination=False):
        
        if self.nodes_table==None:
            self.nodes_table=[]
        if is_source:
            self.nodes_table=[node]+self.nodes_table
        elif is_destination:
            self.nodes_table=self.nodes_table+[node]
        else:
            self.nodes_table.insert(max(len(self.nodes_table)-1,1),node)
        self.nodes_table=list(dict.fromkeys(self.nodes_table))

    
    def add_weighted_edge(self,prec,succ,weight:tuple):
        if self.weighted_edges_table==None:
            self.weighted_edges_table=[]
        self.weighted_edges_table.append((prec,succ,weight))
    
    def add_position(self,node,position:tuple):
        self.nodes_positions[node]=position
    
    def show(self,node_color="lightblue"):
        self.graph=nx.DiGraph() if self.symetric==False else nx.Graph()
        self.graph.add_nodes_from(self.nodes_table)
        self.graph.add_weighted_edges_from(self.weighted_edges_table)
        edge_labes={(i[0],i[1]): str(i[2]) for i in self.weighted_edges_table}
        plt.figure()
        print(len(self.nodes_positions),len(self.nodes_table))
        if len(self.nodes_table)==len(self.nodes_positions):

            pos=self.nodes_positions
        else :

            pos=nx.spring_layout(self.graph)
        try:
            nx.draw(
                self.graph,
                pos=pos,
                node_size=3000,
                with_labels=True,
                node_color=node_color,
                font_size=10,
                arrows=True if self.symetric==False else False)
        except:
            return
        nx.draw_networkx_edge_labels(
            self.graph,
            pos=pos,
            edge_labels=edge_labes
            )
        plt.show()

        
nodes_list = ["Start", "A", "B", "C", "D", "End"]
edges_list = [
    ("Start", "A", 4),
    ("Start", "B", 2),
    ("A", "C", 5),
    ("B", "C", 1),
    ("B", "D", 6),
    ("C", "D", 3),
    ("C", "End", 8),
    ("D", "End", 2)
]
positions_dict = {
    "Start": (0, 0),
    "A":     (1, 1),
    "B":     (1, 0),
    "C":     (2, 1),
    "D":     (2, 0),
    "End":   (3, 0)
}
print(len(positions_dict),len(nodes_list))
# --- INSTANTIATE THE GRAPH ---
# We pass the data directly into the constructor
g = graph(
    nodes_table=nodes_list, 
    weighted_edges_table=edges_list, 
    nodes_positions=positions_dict, 
    symetric=False # False = Directed Graph (Arrows)
)

# Optional: Explicitly mark Source and Destination if your logic requires it
# (Though they are already in the list, this sets flags if you use them later)
g.add_node("Start", is_source=True)
g.add_node("End", is_destination=True)

# --- SHOW THE GRAPH ---
g.show()