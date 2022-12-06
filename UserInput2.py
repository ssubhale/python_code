# Arithmatic operations with get values from user input in function

def Addition(no1,no2):
    return no1 + no2

def Substraction(no1,no2):
    if no1 < no2:
        no1, no2 = no2, no1
    return no1 - no2

def main():
    x = int(input("Enter first value : "))
    y = int(input("Enter second value : "))

    add = Addition(x,y)
    print("Addition is : ",add)

    sub = Substraction(x,y)
    print("Substraction is : ",sub)


if __name__ == "__main__":
    main()
