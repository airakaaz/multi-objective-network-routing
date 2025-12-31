def get_dijkstra_path(graph, table, dest=None):
    if not dest:
        if not graph.dest:
            raise ValueError(
                "no destination specified and graph has no default destination"
            )
        else:
            dest = graph.dest.id

    if dest not in table:
        raise ValueError("destination not found, graph might not be connexe")

    path = []
    curr = dest

    while table[curr][1] != 0:
        path.append(curr)
        curr = table[curr][0]

    path.append(curr)

    path.reverse()

    return path
