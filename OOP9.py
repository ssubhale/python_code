# Design class give the elements of list from user display the list find the maximum number form list

class Number:
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

    def Maximum(self):
        mx = self.seq[0]
        for i in range(self.size):
            if (self.seq[i] > mx):
                mx = self.seq[i]
        print("maximum element of list is : ",mx)

def main():
    obj = Number()
    obj.Accept()
    obj.Display()
    obj.Maximum()

if __name__ == "__main__":
    main()