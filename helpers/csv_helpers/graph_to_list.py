from models.graph_2 import graph

def graph_to_list(g:graph):
    L=[]
    L.append(1 if g.symetric else 0)
    L.append([g.nodes_table[0]])
    L.append([g.nodes_table[2]])
    for i in g.weighted_edges_table:
        L.append([i[0],i[1],i[2][0],i[2][1]])
    return L