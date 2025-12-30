def comb_gen(a, b):
    def combiner(lat, risk):
        return a * lat + b * risk

    return combiner


def path_stats(graph, path):
    lat = risk = 0
    curr = path[0]
    print(curr, end=" ")

    for hop in path[1:]:
        print("->", hop, end=" ")
        edge = graph.edges[(curr, hop)]
        lat += edge[0]
        risk += edge[1]
        curr = hop

    print()
    print("total latency:", lat)
    print("total risk", risk)

    return (lat, risk)
