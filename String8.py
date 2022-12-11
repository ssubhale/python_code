# Find output list from input two list

# l1 = ["Hello","Bye"]
# l2 = ["Pune","Mumbai"]

# o/p :  ["Hello Pune","Hello Mumbai","Bye Pune","Bye Mumbai"] without using any built-in function.

def Function(seq1,seq2):
    l = list()
    for i in seq1:
        for j in seq2:
            l.append(i+" "+j)
    return l


def main():
    print("Application for demonstration of list")
    l1 = ["Hello","Bye"]
    l2 = ["Pune","Mumbai"]
    ans = Function(l1,l2)
    print("Output list : ",ans)

if __name__ == "__main__":
    main()