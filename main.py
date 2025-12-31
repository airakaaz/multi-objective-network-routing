from tkinter import filedialog

from models import Graph
from algorithms import dijkstra, pareto_front, floyd_warshall
from helpers import (
    choose,
    comb_gen,
    get_dijkstra_path,
    get_floyd_path,
    path_stats,
    select_pareto_path,
)


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
    choice = int(
        choose(
            """mode:
                [1]: minimize latency
                [2]: minimize risk
                [3]: custom: weight = a*latency + b*risk
                [0]: cancel
            ---> """,
            lambda c: int(c) in (0, 1, 2, 3),
        )
    )
    match choice:
        case 1:
            a, b = 1, 0
        case 2:
            a, b = 0, 1
        case 3:
            a = int(
                choose(
                    "             a = ",
                    lambda a: int(a) > 0,
                    "a must be strictly positive",
                )
            )
            b = int(
                choose(
                    "             b = ",
                    lambda b: int(b) > 0,
                    "b must be strictly positive",
                )
            )
        case 0:
            return

    src = choose(
        "pick source (leave empty for default graph source):",
        lambda n: (n in graph.nodes or n == ""),
    )
    if not src:
        src = graph.src.id

    table = dijkstra(graph, comb_gen(a, b), src)

    flag = True
    while flag:
        dest = choose(
            "pick destination (leave empty for default graph destination):",
            lambda n: (n in graph.nodes or n == ""),
        )
        if not dest:
            dest = graph.dest.id

        path_stats(graph, get_dijkstra_path(graph, table, dest=dest))

        flag = int(
            choose(
                """pick another destination ?
                    [1]: yes
                    [0]: no
                ---> """,
                lambda x: int(x) in (0, 1),
            )
        )


def use_floyd_warshall(graph):
    choice = int(
        choose(
            """mode:
                [1]: minimize latency
                [2]: minimize risk
                [3]: custom: weight = a*latency + b*risk
                [0]: cancel
            ---> """,
            lambda c: int(c) in (0, 1, 2, 3),
        )
    )

    match choice:
        case 1:
            a, b = 1, 0
        case 2:
            a, b = 0, 1
        case 3:
            a = int(
                choose(
                    "             a = ",
                    lambda a: int(a) > 0,
                    "a must be strictly positive",
                )
            )
            b = int(
                choose(
                    "             b = ",
                    lambda b: int(b) > 0,
                    "b must be strictly positive",
                )
            )
        case 0:
            return

    table = floyd_warshall(graph, comb_gen(a, b))

    flag = True
    while flag:
        src = choose(
            "pick source (leave empty for default graph source):",
            lambda n: (n in graph.nodes or n == ""),
        )
        if not src:
            src = graph.src.id

        dest = choose(
            "pick destination (leave empty for default graph destination):",
            lambda n: (n in graph.nodes or n == ""),
        )
        if not dest:
            dest = graph.dest.id

        path_stats(graph, get_floyd_path(graph, table, src=src, dest=dest))

        flag = int(
            choose(
                """pick another path ?
                    [1]: yes
                    [0]: no
                ---> """,
                lambda x: int(x) in (0, 1),
            )
        )


def use_pareto_front(graph):
    src = choose(
        "pick source (leave empty for default graph source):",
        lambda n: (n in graph.nodes or n == ""),
    )
    if not src:
        src = graph.src.id

    table = pareto_front(graph, src=src)

    flag = True
    while flag:
        dest = choose(
            "pick destination (leave empty for default graph destination):",
            lambda n: (n in graph.nodes or n == ""),
        )
        if not dest:
            dest = graph.dest.id
        choice = int(
            choose(
                """criteria:
                    [1]: minimize latency
                    [2]: minimize risk
                    [3]: custom: weight = a*latency + b*risk
                    [4]: minimize latency with threshold on risk
                    [5]: minimize risk with threshold on latency
                    [0]: cancel
                ---> """,
                lambda c: int(c) in (0, 1, 2, 3, 4, 5),
            )
        )

        match choice:
            case 1:
                path_stats(graph, select_pareto_path(graph, table, 1, 0, dest=dest))
            case 2:
                path_stats(graph, select_pareto_path(graph, table, 0, 1, dest=dest))
            case 3:
                a = int(
                    choose(
                        "             a = ",
                        lambda a: int(a) > 0,
                        "a must be strictly positive",
                    )
                )
                b = int(
                    choose(
                        "             b = ",
                        lambda b: int(b) > 0,
                        "b must be strictly positive",
                    )
                )
                path_stats(graph, select_pareto_path(graph, table, a, b, dest=dest))
            case 4:
                t = int(
                    choose(
                        "     threshold = ",
                        lambda t: int(t) > 0,
                        "a must be strictly positive",
                    )
                )
                path_stats(graph, select_pareto_path(graph, table, None, t, dest=dest))
            case 5:
                t = int(
                    choose(
                        "     threshold = ",
                        lambda t: int(t) > 0,
                        "a must be strictly positive",
                    )
                )
                path_stats(graph, select_pareto_path(graph, table, t, None, dest=dest))
            case 0:
                return

        flag = int(
            choose(
                """pick another criteria/destination ?
                [1]: yes
                [0]: no
            ---> """,
                lambda x: int(x) in (0, 1),
            )
        )


def get_path(graph):
    choice = int(
        choose(
            """algorithms:
            [1]: dijkstra
            [2]: floyd marshall
            [3]: pareto front
            [0]: return
        ---> """,
            lambda c: int(c) in (0, 1, 2, 3),
        )
    )

    match choice:
        case 1:
            use_dijkstra(graph)
        case 2:
            use_floyd_warshall(graph)
        case 3:
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
