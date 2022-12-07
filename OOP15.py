# Write a program to find factorial of a number

class Number:
    def __init__(self,no):
        self.no = no

    def Factorial(self):
        fact = 1
        for i in range(self.no,0,-1):
            fact = fact * i
        return fact

def main():
    print("Application for find the factorial of number")
    num = int(input("Enter a number for find factorial : "))

    obj = Number(num)
    ans = obj.Factorial()
    print(f"Factorial of {num} is : ",ans)

if __name__ == "__main__":
    main()


