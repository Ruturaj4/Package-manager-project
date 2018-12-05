import json
import operator

dic = {}


def main():
    with open("pwn.json", "r") as f:
        f = json.load(f)

    for key,values in f.items():
        try:
            temp = {}
            temp[key] = values["downloads"]
            dic.update(temp)
        except:
            print("Error")
    #with open("top_downloads.json", "w") as fl:
    #    json.dump(dic, fl)
    #print(len(dic))
    with open("pwnall.list", "w") as f:
        for line in dic:
            f.write(str(line))
            f.write("\n")

if __name__ == "__main__":
    main()
