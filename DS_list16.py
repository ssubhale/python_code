# Write a program to calculate occurence of integer. get integer from user

class Classifier:
    def __init__(self,seq,no):
        self.seq = seq
        self.no = no
        self.res = 0

    def Occurence(self):
        for i in self.seq:
            if i == self.no:
                self.res += 1
        return self.res


def main():
    print("Application for find the occurence of user number in predefined list")
    data = [32,5,6,2,0,6,7,0,0,4,5,6,6,3,4,7,8,9,12]
    num = int(input("Enter number for check occurence : "))

    obj = Classifier(data,num)
    ans = obj.Occurence()
    print(f"Occurence of {num} is :",ans)

if __name__ == "__main__":
    main()
