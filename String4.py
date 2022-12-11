# Return the total count of string "Shree" appears in the given string without using count method and with using count method.


def WithCount(seq):
    return seq.count("Shree")


def WithoutCount(seq):
    count = 0
    for i in seq.split():
        if i == "Shree":
            count += 1
    return count


def main():
    print("Application for demonstration of string")
    s = 'Shree is good developer. Shree is honest'

    ans1 = WithCount(s)
    print("Answer with count method : ",ans1)

    ans2 = WithoutCount(s)
    print("Answer without count method : ",ans2)
    

if __name__ == "__main__":
    main()