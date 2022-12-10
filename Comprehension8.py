# Given a list convert into dictionary keys are small letters and values are capital letters


def Program(seq):
    d = {i.lower():i.upper() for i in seq}
    return d

def main():
    print("Application for demonstration of dictionary comprehension")
    data = ["Red", "Green", "Blue","Yellow"]
    ans = Program(data)
    print("Dictionary : ",ans)

if __name__ == "__main__":
    main()

