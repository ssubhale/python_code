
#_4.Program to check elelments in list are divisible by a no. taken by user and creat a separate the list of divisible elements.

class Classifier:
    def __init__(self,seq,no):
        self.seq = seq
        self.no = no

    def Divisible(self):
        div = []
        for i in self.seq:
            if i % self.no == 0:
                div.append(i)
        return div

def main():
    print("Application for create list of divisible numbers in list by users number")
    data = [3,4,78,56,34,23,67,89,32,12,54,65]
    num = int(input("Enter number : "))

    obj = Classifier(data,num)
    ans = obj.Divisible()
    print("Predefined list is : ",data)
    print(f"list of divisible by {num} is : ",ans)


if __name__ == "__main__":
    main()
