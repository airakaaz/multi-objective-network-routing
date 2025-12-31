from models.graph_2 import graph
from helpers.graph_2_constructor import graph_constructor
from csv_helpers.list_to_csv import list_to_csv
from helpers.csv_helpers.graph_2_to_list import graph_to_list
def graph_2_to_csv(g:graph):
    lg=graph_to_list(g)
    return list_to_csv(L=lg)