
#3 Difference - It gives unique elements of first set
#operator is -

def SetDifference(A,B):
    print(A-B)
    print(A.difference(B))


def main():
    A = {1,2,3,4,5}
    B = {4,5,6,7,8}

    SetDifference(A,B)

if __name__ == "__main__":
    main()