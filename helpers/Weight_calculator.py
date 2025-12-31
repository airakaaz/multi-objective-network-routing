from models.graph_2 import graph


def Weight_calculator(latency,risk,latency_priority=1,risk_priority=10):
    return latency_priority*latency+risk_priority*risk

