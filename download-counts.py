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

def downloadCounts(today, package):
    # I have chosen the start date as 2014-01-01 to fetch all of the packages
    url = "https://api.npmjs.org/downloads/point/" + "2014-01-01:" + today + "/" +  package
    r = urllib.request.urlopen(url)
    data = r.read().decode("utf-8")
    dic = json.loads(data)
    print(package)
    return {package:str(dic["downloads"])}



def main():
    graph()
    print(len(G))
    # Today's date
    today = date.today().strftime('%Y-%m-%d')
    # Create a dictionary to append
    data = {}
    print(today)
    for node in G:
        package = node
        data.update(downloadCounts(today, package))
    with open("downloadCounts.json", "w") as f:
        json.dump(data, f)


if __name__ == '__main__':
    main()
