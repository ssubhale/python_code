# In class accept values from user create and display list, print the average of all elements

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
        print("Your list is : ",self.seq)

    def Average(self):
        sum = 0
        for i in self.seq:
            sum += i
        avg = (sum/self.size)
        print("Average of list elements : ",avg)

def main():
    obj = Numbers()
    obj.Accept()
    obj.Display()
    obj.Average()

if __name__ == "__main__":
    main()
