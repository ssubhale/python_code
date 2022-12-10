# Create a new dictionary by extracting the following keys from a given dictionary


def DictComp(dict,keys):
    d = {i:dict[i] for i in keys}
    return d


def main():
    print("Application for demonstration of dictionary comprehension")
    sampleDict = {"name":"Kelly","age":25,"salary":8000,"city":"New york"}
    keys = ["name", "salary"]

    ans = DictComp(sampleDict,keys)
    print("Dictionary : ",ans)

if __name__ == "__main__":
    main()