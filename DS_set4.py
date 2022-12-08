###Mathematical operations on sets

#1 Union - it combines two sets by removing duplicates
# operator is |(py operator) #union method

def SetUnion(A,B):
    print(A|B)
    print(A.union(B))
    

def main():

    A = {1,2,3,4,5}
    B = {4,5,6,7,8}

    SetUnion(A,B)

if __name__ == "__main__":
    main()
