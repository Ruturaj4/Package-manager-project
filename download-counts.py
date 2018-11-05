# Author - Ruturaj Kiran Vaidya

import json
# Importing networkx package
import networkx as nx
from networkx.readwrite import json_graph
import numpy as np
import operator

import pprint
pp = pprint.PrettyPrinter(indent = 4)

# G is a graph
G = nx.DiGraph()


def graph():
    # d is a dictionary
    d = {}
    # Importing json data as a dictionary
    with open("mewpackaged.json", encoding="utf-8") as file:
        d = json.loads(file.read())

    for key, value in d.items():
        #print(value)
        values = {}
        values = value
        #G.add_node(key)
        #f.write(values)
        for k, v in values.items():
            #print(v)
            G.add_edge(key, k)
    print(len(G))


def main():
    graph()


if __name__ == '__main__':
    main()
