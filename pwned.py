import json


def select(top):
    topdic = {}
    for key,value in top.items():
        dic = []
        for entry in value:
            try:
                dic.append(entry["email"])
            except:
                pass
        #print(dic)
        topdic[key] = dic
    print(topdic)
    with open("email.json", "w") as f:
        json.dump(topdic, f)

def main():
    with open("maintainers.json", "r") as f:
        top = json.load(f)
    select(top)

if __name__ == '__main__':
    main()

