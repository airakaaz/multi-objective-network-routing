def floyd_warshall(graph, weight_func):
    table = {n: {n: (0, n)} for n in graph.nodes}
    for (src, dest), weights in graph.edges.items():
        table[src][dest] = (weight_func(*weights), src)

    for u in graph.nodes:
        for v in graph.nodes:
            for w in graph.nodes:
                # check if distance from v to u is infinite
                try:
                    table[v][w]
                    inf = False
                except KeyError:
                    inf = True

                # check if path u->v->w exists
                try:
                    table[v][u]
                    table[u][w]
                    ext = True
                except KeyError:
                    ext = False

                if ext:
                    if inf or table[v][u][0] + table[u][w][0] < table[v][w][0]:
                        table[v][w] = (table[v][u][0] + table[u][w][0], table[u][w][1])
    return table
