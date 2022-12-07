# Design class and create dynamic list of integers and display list, find average of elements, addition of elements and find maximum, minimum element of list

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

    def Addition(self):
        sum = 0
        for i in self.seq:
            sum += i
        print("Addition of elements in list : ",sum)

    def Average(self):
        sum = 0
        for i in self.seq:
            sum += i
        avg = (sum/self.size)
        print("Average of list element is : ",avg)

    def Maximum(self):
        mx = self.seq[0]
        for i in range(self.size):
            if (self.seq[i] > mx):
                mx = self.seq[i]
        print("Maximum element in list is : ",mx) 

    def Minimum(self):
        mn = self.seq[0]
        for i in range(self.size):
            if (self.seq[i] < mn):
                mn = self.seq[i]
        print("Minimum element in list is : ",mn)
                   
def main():
    obj = Numbers()
    obj.Accept()
    obj.Display()
    obj.Average()
    obj.Maximum()
    obj.Minimum()

if __name__ == "__main__":
    main()