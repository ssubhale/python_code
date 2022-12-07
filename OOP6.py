# All arithmatic operations in one class

class Arithmatic:
    def __init__(self,A,B):
        print("Inside __init__ method")
        self.no1 = A
        self.no2 = B

    def Addition(self):
        return self.no1 + self.no2

    def Substraction(self):
        return self.no1 - self.no2

    def Multiplication(self):
        return self.no1 * self.no2

    def Division(self):
        return self.no1 / self.no2

    def FlooDivision(self):
        return self.no1 // self.no2

    def Modulous(self):
        return self.no1 % self.no2

    def Exponent(self):
        return self.no1 ** self.no2

def main():
    print("Inside main function")

    a,b = 16,5
    print(f"Your values are : {a}, {b}")
    obj1 = Arithmatic(a,b)

    add = obj1.Addition()
    print("Addition is : ",add)

    sub = obj1.Substraction()
    print("Substraction is : ",sub)

    mul = obj1.Multiplication()
    print("Multiplication is : ",mul)

    div = obj1.Division()
    print("Division is : ",div)

    fd = obj1.FlooDivision()
    print("Floordivision is : ",fd)

    mod = obj1.Modulous()
    print("Modulous is : ",mod)

    exp = obj1.Exponent()
    print("Exponent is : ",exp)

if __name__ == "__main__":
    main()



