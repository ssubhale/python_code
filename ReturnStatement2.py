# All arithmatic operations with return statement

def Addition(no1,no2):
    ans = no1 + no2
    return ans

def Substraction(no1,no2):
    ans = no1 - no2
    return ans

def Multiplication(no1,no2):
    ans = no1 * no2
    return ans

def Division(no1,no2):
    ans = no1 / no2
    return ans

def FloorDivision(no1,no2):
    ans = no1 // no2
    return ans

def Modulous(no1,no2):
    ans = no1 % no2
    return ans

def Exponent(no1,no2):
    ans = no1 ** no2
    return ans

def main():
    x = 15
    y = 4
    add = Addition(x,y)
    print("Addition is : ",add)

    sub = Substraction(x,y)
    print("Substraction is : ",sub)

    mul = Multiplication(x,y)
    print("Multiplication is : ",mul)

    div = Division(x,y)
    print("Division is : ",div)

    fd = FloorDivision(x,y)
    print("Floor division is : ",fd)

    mod = Modulous(x,y)
    print("Modulous is : ",mod)

    exp = Exponent(x,y)
    print("Exponent is : ",exp)
    
if __name__ == "__main__":
    main()