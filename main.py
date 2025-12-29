from model import Graph
from helpers import combine, path_stats
from algorithms import dijkstra

if __name__ == "__main__":
    graph = Graph(combine, path="data.csv")
    path = dijkstra(graph, combine)
    path_stats(graph, path)
    graph.visualize()
