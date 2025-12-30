from models import Graph
from helpers import comb_gen, path_stats
from algorithms import dijkstra

if __name__ == "__main__":
    balanced = comb_gen(1, 10)
    min_lat = comb_gen(1, 0)
    min_risk = comb_gen(0, 1)
    graph = Graph(path="data/data.csv")
    print("balanced path :")
    path_stats(graph, dijkstra(graph, balanced))
    print("minimum latency path :")
    path_stats(graph, dijkstra(graph, min_lat))
    print("minimum risk path :")
    path_stats(graph, dijkstra(graph, min_risk))
    graph.visualize(balanced)
