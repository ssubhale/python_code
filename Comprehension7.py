# Delete set of keys from Python Dictionary by dictionary comprehension


def DictComp(sdict,ktr):
    d = {k:sdict[k] for k in sdict.keys() - ktr}
    return d


def main():
    print("Application for demonstration of dictionary comprehension")
    sampleDict = {"name": "Kelly","age":25,"salary": 8000,"city": "New york"}
    keysToRemove = ["name", "salary"]

    ans = DictComp(sampleDict,keysToRemove)
    print(ans)

if __name__ == "__main__":
    main()
