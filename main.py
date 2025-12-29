from model import Graph
from helpers import combine

if __name__ == "__main__":
    graph = Graph(combine, path="data.csv")
    graph.visualize()
