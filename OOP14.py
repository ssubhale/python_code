 # Write a program to find factors of number

class Number:
    def __init__(self,no):
        self.no = no

    def Factors(self):
        ftr = []
        for i in range(1,int(self.no/2)+1,1):
            if self.no % i == 0:
                ftr.append(i)
        return ftr


def main():
    print("Application to find factors of number")
    no = int(input("Enter a number:"))
    obj = Number(no)
    ans = obj.Factors()
    print(f"Factors of {no} is ",ans)        

if __name__ == "__main__":
    main()