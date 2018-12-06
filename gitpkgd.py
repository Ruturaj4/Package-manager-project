# Author - Ruturaj Kiran Vaidya
# Requires pymongo 3.6.0+
import pprint
import json
from bson.regex import Regex
from pymongo import MongoClient
# Importing graph package
#import networkx as nx
#G = nx.Graph()

import sys
import time

# Requests
import urllib.request

# Connect to the client
client = MongoClient("mongodb://localhost:27017/")
# Connect to final, which is ut dataset in this case
database = client["final"]
# Our collection is all-docs
collection = database["all-docs"]

# Query and projection model is Created with Studio 3T, the IDE for MongoDB - https://studio3t.com/

# We will keep the query blank
query = {}
#query["doc.versions"] = Regex(u".*dependencies.*", "i")

projection = {}
# Selecting just an id, that would be used to recognize the sub-dictionaries
projection["id"] = 1.0
# Selecting doc.versions to get the dependacies key
projection["doc.versions"] = 1.0
#projection["doc.versions.1.0.0.dependencies"] = 1.0

# This is the actual query
cursor = collection.find(query, projection = projection)
# Yes, I want it pretty!
pp = pprint.PrettyPrinter(depth=4)
d = {}
# Code for versions
#dversions = {}
# ----

try:
    # Iterate through all the docs
    for doc in cursor:
        # Creating a dictionary for individual packages
        packaged = {}
        #pp.pprint(doc.keys())
        pp.pprint(doc["id"])
        #G.add_node(doc["id"])
        # A temporary dictionary, because I'm lazy
        temp_dict = doc["doc"]
        if "versions" in temp_dict:
            temp_dict = doc["doc"]["versions"]
            # Get all the values as list, values as in all the version names, because, as each package has different versions, so version names can't be used to query the database, So we'll iterate through this list
            values = list(temp_dict.values())
            # A dictionary to store the dependencies
            dependency = {}
            # A dictionary to store versons and dependencies
            #dicversions = {}
            # ----
            #pp.pprint(values)
            #for x in values:
            # A dictionary for all the versions of the package
            try:
                if values[-1]:
                    dic = {}
                    dic = values[-1]
                    #print(dic)
                    if "repository" in dic:
                        # Check for a noneType
                        if dic["repository"]["url"] is not None:
                            # dependency = (dic["dependencies"])
                            # Append to the dictionary structure, so the dependencies are global, as in dependacies of the all the versions
                            # Code for versions
                            #dicversions.update(dic["dependencies"])
                            # ----
                            dependency = (dic["repository"]["url"]).replace("ssh://", "")
                            dependency = dependency.replace("git+", "")
                            dependency = dependency.replace("git@", "")
                            dependency = dependency.replace("git://", "")
                            dependency = dependency.replace("github.com", "api.github.com/repos")
                            if dependency.endswith(".git"):
                                dependency = dependency[:-4]
                            if not dependency.startswith("https://"):
                                dependency = "https://" + dependency
                            if "github.com" not in dependency:
                                dependency = {}
                            if dependency == {}:
                                continue
                            else if dependency != {}:
                                try:
                                    time.sleep(1)
                                    r = urllib.request.urlopen(urllib.request.Request(dependency, headers={'Authorization':'token TOKEN'}))
                                    data = r.read().decode("utf-8")
                                    dic = json.loads(data)
                                    print(dependency)
                                    dependency = dic["stargazers_count"]
                                except urllib.error.HTTPError as err:
                                    dependency = {}

            except:
                pass
            if dependency != {}:
                print(dependency)
            # Code for versions
            #pp.pprint(x)
            #dversions[dic["version"]] = dicversions
            # ----
            packaged[doc["id"]] = dependency
            # Code for versions
            #packaged[doc["id"]] = dversions
            # ----
            d.update(packaged)
            #print(len(dependency))
finally:
    # Open packaged.json - for versionless
    f = open("githubid.json", "w")
    f.write(json.dumps(d))
    f.close()
    client.close()
