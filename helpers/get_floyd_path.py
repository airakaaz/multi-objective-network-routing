def get_floyd_path(g, table, src=None, dest=None):
    if not src:
        if not g.src:
            raise ValueError("source not specified and graph has no default source.")
        else:
            src = g.src.id

    if not dest:
        if not g.src:
            raise ValueError(
                "destination not specified and graph has no default destination."
            )
        else:
            dest = g.dest.id

    if not table[src][dest]:
        print(f"no path found from {src} to {dest}")
        return None
    else:
        path = []
        curr = dest
        while curr != src:
            path.append(curr)
            curr = table[src][curr][1]
        path.append(src)
        path.reverse()

        return path
