# Give three string from user like first_name, middle_name, last_name and return the output as full name

def Function(s1,s2,s3):
    return s1 +" "+ s2 +" "+ s3


def main():
    print("Application for demonstration of string")
    a = input("Enter first name : ")
    b = input("Enter middle name : ")
    c = input("Enter last name : ")

    ans = Function(a,b,c)
    print("Your full name is : ",ans)

if __name__ == "__main__":
    main()