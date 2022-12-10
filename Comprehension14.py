# Bellow have to dictionary and find the output dictionary into them by dictionary comprehension

a = {"a":1, "b":2, "c":3}
b = {"az":1, "bz":2, "cz":3}

op = {"az":{"a":1}, "bz":{"b":2}, "cz":{"c":3}}


def Comp(a,b):
    op = {key:{key1: value1} for key,value in b.items() for key1, value1 in a.items() if value==value1}
    return op

def Program(a,b):
    op = dict()
    for key,value in b.items():
        for key1,value1 in a.items():
            if value == value1:
                op[key] = {key1:value1}
    return op


def main():
    print("Application for demonstration of dictionary comprehension")
    a = {"a":1, "b":2, "c":3}
    b = {"az":1, "bz":2, "cz":3}

    res = Comp(a,b)
    print("Output dictionary by comprehension : ",res)

    ans = Program(a,b)
    print("Output dictionary by for loop : ",ans)

if __name__ == "__main__":
    main()
