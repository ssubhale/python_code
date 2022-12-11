# Find output list from given input list

# l1 = ["M","na","i","Sh"]
# l2 = ["y","me","s","ree"]

#o/p : ["My","name","is","Emma"]  without using any built-in function.


def Function(seq1,seq2):
    l = list()
    for i in range(len(seq1)):
        l.append(seq1[i]+seq2[i])
    return l


def main():
    print("Application for demonstration of list")
    l1 = ["M","na","i","Sh"]
    l2 = ["y","me","s","ree"]

    ans = Function(l1,l2)
    print("Output list : ",ans)


if __name__ == "__main__":
    main()