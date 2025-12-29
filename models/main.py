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
        self.source_found=False
        self.destination_found=False
        self.graph=None
        self.symetric=symetric

    def add_node(self,node,is_source=False,is_destination=False):
        
        if self.nodes_table==None:
            self.nodes_table=[]
        if is_source and not(self.source_found):
            self.source_found=True
            self.nodes_table=[node]+self.nodes_table
        elif is_destination and not(self.destination_found):
            self.destination_found=True
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


