import json
import networkx as nx
import time
import operator
# G is a graph
G = nx.DiGraph()

from urllib.request import Request, urlopen

def graph():
    d = {}
    with open("lastPackaged.json", encoding="utf-8") as file:
        d = json.loads(file.read())
    for key, value in d.items():
        #print(value)
        values = {}
        values = value
        #G.add_node(key)
        for k, v in values.items():
            G.add_edge(key, k)

def graph_down(top):
    for node in G.copy():
        if node not in top:
            G.remove_node(node)
    for node in top.copy():
        if node not in G:
            top.pop(node, None)

def popularity(top):
    for node in G:
        print(node)
        print(top[node])
        count = 0
        print (len(G.in_edges(node)))
        for edge in G.in_edges(node):
            #print(edge[0])
            count += top[edge[0]]
        print(top[node] - count)

def pawned(sorted_top):
    with open("email.json", "r") as file:
        email = json.load(file)
    dic = {}
    #for node in G:
        #print(node)
    for key,value in email.items():
        if key in sorted_top:
            print(key)
            li = []
            for emailId in value:
                time.sleep(1.8)
                url = "https://haveibeenpwned.com/api/v2/breachedaccount/" + emailId
                #print(url)
                try:
                    r = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                    webpage = urlopen(r).read()
                    #print(webpage)
                    li.append("pwned")
                    print("P")
                except:
                    li.append("Safe")
                    print("safe")
            dic[key] = li
        with open("pwn.json", "w") as f:
            json.dump(dic, f)

def test():
    emailId = "ruturajkvaidya@gmail.com"
    url = "https://haveibeenpwned.com/api/v2/breachedaccount/" + emailId
    print(url)
    r = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(r).read()
    print(webpage)


def main():
    with open("top_downloads.json", "r") as f:
        top = json.load(f)
    #graph()
    #graph_down(top)
    print(len(G))
    print(len(top))
    #popularity(top)
    #pawned(top)
    sorted_top = sorted(top.items(), key=lambda kv: kv[1], reverse=True)
    sorted_top = [i[0] for i in sorted_top][:1000]
    print(sorted_top)
    pawned(sorted_top)

if __name__ == '__main__':
    main()
