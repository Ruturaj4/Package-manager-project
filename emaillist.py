import json
from bson.regex import Regex
from pymongo import MongoClient

# Connect to the client
client = MongoClient("mongodb://localhost:27017/")
# Connect to final, which is ut dataset in this case
database = client["final"]
# Our collection is all-docs
collection = database["all-docs"]

# We will keep the query blank
query = {}

projection = {}
# Selecting just an id, that would be used to recognize the sub-dictionaries
projection["id"] = 1.0
# Selecting doc.versions to get the dependacies key
projection["doc.versions"] = 1.0


# This is the actual query
cursor = collection.find(query, projection = projection)

d = {}

try:
    for doc in cursor:
        # Creating a dictionary for individual packages
        packaged = {}
        if doc["id"][0] == "@":
            continue
        print(doc["id"])
        temp_dict = doc["doc"]
        if "versions" in temp_dict:
            temp_dict = doc["doc"]["versions"]
            values = list(temp_dict.values())
            dependency = []
            for x in values:
                # A dictionary for all the versions of the package
                dic = {}
                dic = x
                if "maintainers" in dic:
                    # Check for a noneType
                    try:
                        if dic["maintainers"] is not None:
                            dependency = (dic["maintainers"])
                            print(dependency)
                    except:
                        pass
            packaged[doc["id"]] = dependency
            d.update(packaged)
finally:
    f = open("maintainers.json", "w")
    f.write(json.dumps(d))
    f.close()
    client.close()
