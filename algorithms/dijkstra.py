def dijkstra(graph, weight_func):
    if graph.src is None:
        raise Exception("no source in graph")
    if graph.dest is None:
        raise Exception("no destination in graph")

    table = {graph.src.id: (graph.src.id, 0)}
    unvisited = set(node for node in graph.nodes)

    while unvisited:
        candidates = {k: v for k, v in table.items() if k in unvisited}
        if not candidates:
            break  # in case graph is not convex
        curr = graph.nodes[min(candidates, key=lambda n: candidates[n][1])]
        unvisited.remove(curr.id)

        if curr == graph.dest:
            break

        for node in curr.successors:
            if node.id not in unvisited:
                continue

            lat, risk = graph.edges[(curr.id, node.id)]
            weight = weight_func(lat, risk)
            if weight < 0:
                raise Exception(
                    f"weight function '{weight_func.__name__}' computed negative weight on edge {(curr.id, node.id)}:{graph.edges[(curr.id, node.id)]}"
                )
            dist = table[curr.id][1] + weight

            if node.id not in table or dist < table[node.id][1]:
                table[node.id] = (curr.id, dist)

    if curr is not graph.dest:
        print("destination is unreachable, the graph might not be connexe")
        return None

    path = []
    curr_id = curr.id
    while curr_id != graph.src.id:
        path.insert(0, curr_id)
        curr_id = table[curr_id][0]
    path.insert(0, graph.src.id)

    return path
