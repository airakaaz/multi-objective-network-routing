from models.main import graph

def Weight_calculator(latency,risk,latency_priority=1,risk_priority=10):
    return latency_priority*latency+risk_priority*risk

def graph_constructor(g:graph,nodes_number=8,edges_number=12):
    for i in range(nodes_number):
        node=input("Enter the node {i}: ")
        if not(g.source_found):
            is_source=int(input("is it the source: "))
        if not(g.destination_found) and not(is_source):
            is_destination=int(input("Is it the "))
        g.add_node(node,is_source=is_source,is_destination=is_destination)
    j=0
    while j<edges_number:
        try:
            prec,succ=input("Enter the prec and the succ \n(format: prec,succ)\n").split(",")
            weight=tuple(input("Enter the latency and the risk \n(format: latency,risk)\n").split(","))
            weight=Weight_calculator(weight[0],weight[1])
            g.add_weighted_edge(prec=prec,succ=succ,weight=weight)
            j+=1
        except:
            print("the Entered values should be like the given format!")
        
    return g

