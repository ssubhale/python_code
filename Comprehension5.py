# Convert two lists into dictionary by dictionary comprehension

def DictComp(keys,values):
    d = {keys[j]:values[j] for j in range(len(keys))}
    return d


def main():
    print("Application for demonsttration of dictioanry comprehension")
    keys = ['Ten','Twenty','Thirty']
    values = [10,20,30]
    ans = DictComp(keys,values)
    print("Dictionary : ",ans)

if __name__ == "__main__":
    main()

