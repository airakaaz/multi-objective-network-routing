import heapq


def dijkstra(graph, weight_func, src=None):
    if not src:
        if not graph.src:
            raise ValueError("no source specified and graph has no default source")
        else:
            src = graph.src.id

    table = {src: (src, 0)}
    visited = set()
    candidates = [(0, src)]

    while candidates:
        _, curr = heapq.heappop(candidates)
        curr = graph.nodes[curr]
        visited.add(curr)

        for node in curr.successors:
            if node.id in visited:
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
                heapq.heappush(candidates, (weight, node.id))

    return table
