# Bellow list is given find the following output list by list comprehension

Input = [2,3,4,5,6,"krishna"]
Output = [10,15,20,25,30,"Shrikrishna"]

def Comp(seq):
    l = ["Shri"+i if type(i) == str else i*5 for i in seq]
    return l


def Program(seq):
    l = list()
    for i in seq:
        if type(i) == str:
            l.append("Shri"+i)
        else:
            l.append(i*5)
    return l


def main():
    print("Application for demonstration of list comprehension")
    data = [2,3,4,5,6,"krishna"]

    res = Comp(data)
    print("Output list by comprehension : ",res)

    ans = Program(data)
    print("Output list by for loop : ",ans)

if __name__ == "__main__":
    main()
