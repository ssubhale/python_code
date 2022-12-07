# check the number is prime or not

class Value:

    def __init__(self,no):
        self.no = no

    def checkPrime(self):
        count = 0
        flage = False
        for i in range(1,int(self.no/2)+1):
            if (self.no % i == 0):
                # print(i)
                count += 1

        if count == 1:
            flage = True
        else:
            flage = False
            
        return flage


def main():
    num = int(input("Enter a number : "))

    obj = Value(num)
    res = obj.checkPrime()
    if (res == True):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

if __name__ == "__main__":
    main()