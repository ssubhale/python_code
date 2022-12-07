# Design class give the elements of list from user display the list find the minimum number form list

class Numbers:
    def __init__ (self):
        self.size = 0
        self.seq = list()

    def Accept(self):
        self.size = int(input("Enter how many elements you want in list : "))
        for i in range(self.size):
            value = int(input("Enter value : "))
            self.seq.append(value)

    def Display(self):
        print("Your list is : ",self.seq)

    def Minimum(self):
        mn = self.seq[0]
        for i in range(self.size):
            if (self.seq[i]) < mn:
                mn = self.seq[i]
        print("Minimum element in list is : ",mn)

def main():
    obj = Numbers()
    obj.Accept()
    obj.Display()
    obj.Minimum()

if __name__ == "__main__":
    main()
