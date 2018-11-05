# Author - Ruturaj Kiran Vaidya

import json
# Importing networkx package
import networkx as nx

import urllib.request
from datetime import date

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

def downloadCounts():
    url = "https://api.npmjs.org/downloads/point/" + "last-day" +  "/node"
    r = urllib.request.urlopen(url)
    dic = {}
    data = r.read().decode("utf-8")
    dic = json.loads(data)
    print(dic["downloads"])


def main():
    #graph()
    #print(len(G))
    downloadCounts()


if __name__ == '__main__':
    main()
