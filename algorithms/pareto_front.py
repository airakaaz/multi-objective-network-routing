from collections import deque


def addup(cost, increase):
    return (cost[0] + increase[0], cost[1] + increase[1])


def dominate(o, n):
    if all(x <= y for x, y in zip(o, n)):
        return -1
    if all(x >= y for x, y in zip(o, n)) and any(x > y for x, y in zip(o, n)):
        return 1
    return 0


def pareto_front(graph, src=None):
    if not src:
        if not graph.src:
            raise ValueError("no source specified and graph has no default source")
        else:
            src = graph.src.id

    queue = deque([graph.nodes[src]])
    table = {}
    for node in graph.nodes.values():
        table[node.id] = []
    table[src] = [{"cost": (0, 0), "path": [src]}]

    while queue:
        curr = queue.popleft()

        for node in curr.successors:
            for path in table[curr.id]:
                new_cost = addup(path["cost"], graph.edges[(curr.id, node.id)])

                valid = True
                dominated = []
                for opt in table[node.id]:
                    if valid:
                        match dominate(opt["cost"], new_cost):
                            case -1:
                                valid = False
                            case 0:
                                continue
                            case 1:
                                dominated.append(opt)
                    else:
                        break

                for opt in dominated:
                    table[node.id].remove(opt)

                if valid:
                    table[node.id].append(
                        {"cost": new_cost, "path": path["path"] + [node.id]}
                    )
                    if node not in queue:
                        queue.append(node)

    return table
