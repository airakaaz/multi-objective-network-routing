from numpy import block, select
from models import Graph
from helpers import comb_gen, path_stats, select_path
from algorithms import dijkstra, pareto_front


def demo(path="data/demo.csv"):
    graph = Graph(path=path)

    balanced = comb_gen(1, 10)
    min_lat = comb_gen(1, 0)
    min_risk = comb_gen(0, 1)

    print("### DIJKSTRA ###")
    print("balanced path (weight = 1*latency + 10*risk):")
    path_stats(graph, dijkstra(graph, balanced))
    print()
    print("minimum latency path (weight = 1*latency + 0*risk):")
    path_stats(graph, dijkstra(graph, min_lat))
    print()
    print("minimum risk path (weight = 0*latency + 1*risk):")
    path_stats(graph, dijkstra(graph, min_risk))
    print("################\n\n")

    print("### PARETO FRONT ###")
    opts = pareto_front(graph)
    if opts:
        print("minimum latency path:")
        path_stats(graph, select_path(opts, 1, 0))
        print()
        print("minimum risk path:")
        path_stats(graph, select_path(opts, 0, 1))
        print()
        print("balanced path:")
        path_stats(graph, select_path(opts, 1, 10))
        print()
        print("minimum latency path with risk threshold = 5:")
        path_stats(graph, select_path(opts, None, 5))
        print()
        print("minimum risk path with latency threshold = 100:")
        path_stats(graph, select_path(opts, 100, None))
    print("####################\n\n")

    graph.visualize(block=True)


if __name__ == "__main__":
    demo()
