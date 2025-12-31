from tkinter import filedialog

from models import Graph
from algorithms import dijkstra, pareto_front
from helpers import choose, comb_gen, path_stats, select_path


def graph_selector():
    flag = True
    while flag:
        flag = False
        try:
            print()
            choice = int(
                input("""options:
    [1]: use demo graph
    [2]: import your own graph from file
    [3]: show supported file structure for graph
    [0]: exit
---> """)
            )
        except ValueError:
            print("invalid option")
            choice = None

        match choice:
            case 1:
                g = Graph(path="data/demo.csv")
            case 2:
                path = filedialog.askopenfilename()
                if path:
                    g = Graph(path=path)
                else:
                    print("failed to open file")
                    flag = True
            case 3:
                print("""data structure (check data/demo.csv for the demo example):
                0 or 1                          # 1 if symetric, 0 if not
                src_node
                dest_node
                node1,node2,latency,risk        # edges
                """)
                flag = True
            case 0:
                exit()
            case _:
                flag = True
                print("invalid option")

    return g


def use_dijkstra(graph):
    choice = choose(
        """mode:
                [1]: minimize latency
                [2]: minimize risk
                [3]: custom: weight = a*latency + b*risk
                [0]: cancel
            ---> """,
        lambda c: c in (0, 1, 2, 3),
    )
    match choice:
        case 1:
            a, b = 1, 0
        case 2:
            a, b = 0, 1
        case 3:
            a = choose(
                "             a = ", lambda a: a > 0, "a must be strictly positive"
            )
            b = choose(
                "             b = ", lambda b: b > 0, "b must be strictly positive"
            )
        case 0:
            return
    path_stats(graph, dijkstra(graph, comb_gen(a, b)))


def use_pareto_front(graph):
    paths = pareto_front(graph)

    choice = choose(
        """mode:
                [1]: minimize latency
                [2]: minimize risk
                [3]: custom: weight = a*latency + b*risk
                [4]: minimize latency with threshold on risk
                [5]: minimize risk with threshold on latency
                [0]: cancel
            ---> """,
        lambda c: c in (0, 1, 2, 3, 4, 5),
    )

    match choice:
        case 1:
            path_stats(graph, select_path(paths, 1, 0))
        case 2:
            path_stats(graph, select_path(paths, 0, 1))
        case 3:
            a = choose(
                "             a = ", lambda a: a > 0, "a must be strictly positive"
            )
            b = choose(
                "             b = ", lambda b: b > 0, "b must be strictly positive"
            )
            path_stats(graph, select_path(paths, a, b))
        case 4:
            t = choose(
                "     threshold = ", lambda t: t > 0, "a must be strictly positive"
            )
            path_stats(graph, select_path(paths, None, t))
        case 5:
            t = choose(
                "     threshold = ", lambda t: t > 0, "a must be strictly positive"
            )
            path_stats(graph, select_path(paths, t, None))
        case 0:
            return


def get_path(graph):
    choice = choose(
        """algorithms:
            [1]: dijkstra
            [2]: pareto front
            [0]: return
        ---> """,
        lambda c: c in (0, 1, 2),
    )

    match choice:
        case 1:
            use_dijkstra(graph)
        case 2:
            use_pareto_front(graph)
        case 0:
            return


if __name__ == "__main__":
    g = graph_selector()
    print("graph loaded successfully")

    while True:
        try:
            print()
            choice = int(
                input("""options:
        [1]: visualize graph
        [2]: get shortest path
        [3]: load another graph
        [0]: exit
    ---> """)
            )
        except ValueError:
            print("invalid option")
            choice = None

        match choice:
            case 1:
                g.visualize(block=True)
            case 2:
                get_path(g)
            case 3:
                g = graph_selector()
            case 0:
                exit()
            case _:
                print("invalid option")
