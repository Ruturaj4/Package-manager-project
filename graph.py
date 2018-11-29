# Author - Ruturaj Kiran Vaidya

import json
# Importing networkx package
import networkx as nx
from networkx.readwrite import json_graph

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# To sort the dictionary
import operator
import csv

import pandas

import pprint

# G is a graph
G = nx.DiGraph()


max_d = []

def downloadCounts():
    with open("downloadC.json", "r") as f:
        f = json.load(f)
    dic = {}
    for key,values in f.items():
        try:
            temp = {}
            temp[key] = values["downloads"]
            dic.update(temp)
        except:
            pass
    dic = sorted(dic.values(), reverse=True)
    return dic

def graph():
    pp = pprint.PrettyPrinter(indent = 4)
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


# dfs_depth base Code reference networkx
def dfs_depth(G, source=None, depth_limit=None):
    if source is None:
        nodes = G
    else:
        nodes = [source]
    visited = set()
    if depth_limit is None:
        depth_limit = len(G)
    for start in nodes:
        print(start)
        if start in visited:
            continue
        max_depth = 0
        visited.add(start)
        stack = [(start, depth_limit, iter(G[start]))]
        while stack:
            parent, depth_now, children = stack[-1]
            try:
                child = next(children)
                if child not in visited:
                    yield parent, child
                    visited.add(child)
                    if depth_now > 1:
                        if((depth_limit - depth_now + 1)>max_depth):
                            max_depth = depth_limit - depth_now + 1
                        stack.append((child, depth_now - 1, iter(G[child])))
            except StopIteration:
                stack.pop()
    global max_d
    max_d.append(max_depth)


def pageRank():
    #Calculate the page rank
    pr = {}
    pr = nx.pagerank(G)
    pr = sorted(pr.values(), reverse=True)
    return pr
    #sorted_pr = sorted(pr.items(), key=lambda x: x[1], reverse=True)
    #with open("pagerank.list", "a") as f:
    #    for line in sorted_pr:
    #        f.write(str(line))
    #       f.write("\n")

def deplist(dc, pr):
    # Calculate all the dependencies, dependents
    dcon = {}
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    for node in G:
        print(node)
        #temp = {node:len(G.out_edges(node))}
        list1.append(node)
        list2.append(len(G.out_edges(node)))
        list3.append(len(G.in_edges(node)))
        list4.append(len(list(nx.dfs_edges(G,node))))
        list(dfs_depth(G, node))
        #dcon.update(temp)
    list2 = sorted(list2, reverse=True)
    list3 = sorted(list3, reverse=True)
    list4 = sorted(list4, reverse=True)
    global max_d
    max_d = sorted(max_d, reverse=True)
    print(max_d)
    print("Maximums:")
    print(max(list2[:1000]))
    print(max(list3[:1000]))
    print(max(list4[:1000]))
    print(max(pr[:1000]))
    print(max(max_d[:1000]))
    print(max(dc[:1000]))
    print("Minimums:")
    print(min(list2[:1000]))
    print(min(list3[:1000]))
    print(min(list4[:1000]))
    print(min(pr[:1000]))
    print(min(max_d[:1000]))
    print(min(dc[:1000]))
    #sorted_dcon = sorted(dcon.items(), key=lambda x: x[1], reverse=True)
    df = pandas.DataFrame(data={"Dependencies":list2[:1000], "Dependents":list3[:1000], "DFS-Edges":list4[:1000], "Max-Depth":max_d[:1000], "Page Rank":pr[:1000], "Download Counts":dc[:1000]})
    df.plot(kind="density", subplots=True, layout=(3,3), sharex=False)
    plt.show()
    #df.to_csv("allthings.csv", sep=",", index=False)
"""
#print(sorted(maxDepth))
for node in G:
    if (len(G[node])== 0):
        continue
    list(dfs_depth(G, node))
"""
def zero_to_nan(values):
    return [float('nan') if x==0 else x for x in values ]
"""
x = zero_to_nan(max_d)

x = np.sort(x)
print(x)
print(len(x))
p = 1. * np.arange(len(x))/(len(x) - 1)
plt.plot(x, p, marker='.')
_ = plt.xlabel('Maximum Depth')
_ = plt.ylabel('CDF')
plt.margins(0.02)
plt.show()
"""
#nx.write_gml(G,'g.gml')
#nx.write_graphml(G,'g.xml')
"""
li = []
for node in G:
    if "lodash" in list(G[node]):
        li.append(node)
f = open("li.list", "w")
f.write(str(li))
"""
#pp.pprint(T)
#print(dp)
#print(len(G.in_edges("lodash")))
#print(len(G.in_edges("npm")))
#print(len(G.edges("npm")))
####################################################
# Plot of a graph with number of dependencies
"""
objects = ("Connected nodes", "Not-connected nodes")
y_pos = np.arange(len(objects))
number = (501151, 306449)
plt.bar(y_pos, number, align="center", alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel("Nodes")
plt.title("Connected vs Not-connected")
plt.show()
"""
def dependency_graph():
    deplist = []
    
    for node in G:
        if len(G[node]) == 0:
            continue
        deplist.append(len(G.in_edges([node])))
    x = zero_to_nan(deplist)
    x = np.sort(x)
    print(x)
    print(len(x))
    p = 1. * np.arange(len(x))/(len(x) - 1)
    plt.plot(x, p, marker='.', linestyle='none')
    _ = plt.xlabel('Dependents')
    _ = plt.ylabel('CDF')
    plt.margins(0.02)
    plt.show()
    #S = sorted(G.in_degree, key=lambda x: x[1], reverse=True)


def dfsedges():
    deplist = []
    for node in G:
        if (len(G[node]) == 0):
            continue
        #print(node)
        deplist.append(len(list(nx.dfs_edges(G,node))))
    """
    with open('dfs.txt', 'w') as f:
        for item in deplist:
            f.write("%s\n" % item)
    """
    x = zero_to_nan(deplist)
    x = np.sort(x)
    print(len(x))
    p = 1. * np.arange(len(x))/(len(x) - 1)
    plt.plot(x, p, marker='.', linestyle='none')
    _ = plt.xlabel('Nodes')
    _ = plt.ylabel('CDF')
    plt.margins(0.02)
    plt.show()

# Plot of a graph with depth value
"""
deplist = []

for node in G:
    if (len(G[node]) > 0) and (len(G[node]) < 200):
        deplist.append(len(G[node]))

num_bins = 20
counts, bin_edges = np.histogram(deplist, bins=num_bins, normed=True)
cdf = np.cumsum(counts)
plt.plot(bin_edges[1:], cdf)
plt.show()

"""


def main():
    graph()
    dc = downloadCounts()
    pr = pageRank()
    deplist(dc, pr)
    #highest = []
    #for node in G:
    #    if (len(G[node]) == 1000) :
    #        print("This is the node:")
    #        print(node)
    # Print total number of nodes ---- imp
    print("Total number of nodes: ")
    print(len(G))

    #dfsedges()

    ################################
    #various plot
    #dfsedges()
    #dependency_graph()
    #dependency_graph()
    #dependency_graph()


    ################################


    print(len(list(nx.dfs_preorder_nodes(G,"lodash"))))
    print(len(list(nx.dfs_edges(G,"lodash"))))
    print(len(G["bloater"]))
    # Print total number of edges ---- imp
    print(G.number_of_edges())
    print(len(G.edges(["lodash"])))
    print(len(G.edges(["request"])))



if __name__ == '__main__':
    main()
