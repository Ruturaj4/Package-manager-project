# Author - Ruturaj Kiran Vaidya

import json
# Importing networkx package
import networkx as nx

import urllib.request
from datetime import date

# Multiprocessing
from multiprocessing import Process

# G is a graph
G = nx.DiGraph()
# Create a dictionary to append
data = {}


# d is a dictionary
d = {}

def graph():
    # Importing json data as a dictionary
    with open("mewpackaged.json", encoding="utf-8") as file:
        d.update(json.loads(file.read()))

def downloadCounts(today, packages):
    packages = ','.join(map(str, packages))
    print(packages)
    # I have chosen the start date as 2017-11-05 to fetch all of the packages
    url = "https://api.npmjs.org/downloads/point/" + "2017-11-05:" + today + "/" + packages
    try:
        r = urllib.request.urlopen(url)
        d = (r.read().decode("utf-8"))
        d = json.loads(d)
        data.update(d)
        print(d)
        #with open("downloadC.json", "a") as f:
        #    json.dump(data, f)
    except urllib.error.HTTPError as err:
        print("Error")


def main():
    graph()
    # Today's date
    today = date.today().strftime('%Y-%m-%d')
    l = list(d.keys())
    l = [x for x in l if "@" not in x]
    print(len(l))
    j = 0
    for i in range(127, 801751, 127):
        print(j)
        downloadCounts(today, l[j:i])
        j += 127
    print(d)
    with open("downloadC.json", "w") as f:
        json.dump(data, f)

if __name__ == '__main__':
    main()
