from helpers import comb_gen


def get_latency(path):
    return path["cost"][0]


def get_risk(path):
    return path["cost"][1]


def select_path(paths, lat, risk):
    if lat is None and risk is None:
        raise ValueError("l and r cannot both be None")

    elif None in (lat, risk):
        if lat is None:
            if risk < 0:
                raise ValueError("r must be positive")

            candidates = [p for p in paths if get_risk(p) <= risk]
            print(candidates)
            if candidates:
                return min(candidates, key=get_latency)["path"]
            else:
                return min(candidates, key=get_risk)["path"]

        if risk is None:
            if lat < 0:
                raise ValueError("l must be positive")

            candidates = [p for p in paths if get_latency(p) <= lat]
            print(candidates)
            if candidates:
                return min(candidates, key=get_risk)["path"]
            else:
                return min(candidates, key=get_latency)["path"]

    elif lat < 0 or risk < 0:
        raise ValueError("l and r must be positive")

    else:
        combiner = comb_gen(lat, risk)
        return min(paths, key=lambda x: combiner(*x["cost"]))["path"]
