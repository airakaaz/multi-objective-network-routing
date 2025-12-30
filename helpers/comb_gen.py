def comb_gen(a, b):
    def combiner(lat, risk):
        return a * lat + b * risk

    return combiner
