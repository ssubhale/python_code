
#2 Intersection - it returns set of common elements in both the sets
#operator is &

def SetIntersection(A,B):
    print(A&B)
    print(A.intersection(B))

def main():
    A = {1,2,3,4,5}
    B = {4,5,6,7,8}

    SetIntersection(A,B)

if __name__ == "__main__":
    main()

