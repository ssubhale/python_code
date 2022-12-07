# check the number is perfect or not

class Number:
    def __init__ (self,no):
        self.no = no

    def SumFactor(self):
        sum = 0
        for i in range(1,self.no,1):
            if (self.no % i == 0):
                sum += i
        print(sum)
        return sum

    def CheckPerfect(self):
        ans = self.SumFactor()
        print(ans)
        if (self.no == ans):
            print("Its perfect number")
        else:
            print("Its not a perfect number")

        
def main():
    num = int(input("Enter a number to check its perfect or not : "))

    obj = Number(num)
    obj.CheckPerfect()
    
if __name__ == "__main__":
    main()