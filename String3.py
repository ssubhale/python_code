# Accept string from a user and display only those characters which are present at an even index number.

def Function(seq):
    data = ""
    for i in range(len(seq)):
        if i % 2 == 0:
            data = data + seq[i]
    return data


def main():
    print("Application for demonstration of string")
    s = input("Enter s string : ")
    ans = Function(s)
    print("Characters are present on even index in your string : ",ans)

if __name__ == "__main__":
    main()