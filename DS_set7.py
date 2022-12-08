#4 Symmetric_difference - It gives unique elements of both sets
#operator is ^

def SetSymetric(A,B):
    print(A^B)
    print(B.symmetric_difference(A))


def main():
    A = {1,2,3,4,5}
    B = {4,5,6,7,8}

    SetSymetric(A,B)

if __name__ == "__main__":
    main()

