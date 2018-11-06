import json
import operator

dic = {}


def main():
    with open("downloadC.json", "r") as f:
        f = json.load(f)

    for key,values in f.items():
        try:
            temp = {}
            temp[key] = values["downloads"]
            dic.update(temp)
        except:
            print("Error")
    sorted_dic = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
    with open("top_downloads.json", "w") as fl:
        json.dump(dic, fl)
    print(len(dic))

if __name__ == "__main__":
    main()
