# In class accept values from user create and display list, print the sum of all elements

class Numbers:
    def __init__ (self):
        self.size = 0
        self.seq = list()

    def Accept(self):
        self.size = int(input("How many elements you want to add in list : "))
        for i in range(self.size):
            value = int(input("Enter value : "))
            self.seq.append(value)

    def Display(self):
        print("List : ",self.seq)

    def Addition(self):
        sum = 0
        for i in self.seq:
            sum += i
        print("Addition of all elements in list is : ",sum)

def main():
    obj = Numbers()
    obj.Accept()
    obj.Display()
    obj.Addition()

if __name__ == "__main__":
    main()
