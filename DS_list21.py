# Write a program to find second smallest number in list

class Classifier:
    def __init__(self,seq):
        self.seq = seq
        self.smallest = 0
        self.sec_smallest = 0

    def Sec_Smallest(self):
        self.smallest = self.seq[0]
        self.s_smallest = self.seq[0]

        for i in range(len(self.seq)):
            if self.seq[i] < self.smallest:
                self.smallest = self.seq[i]

        for i in range(len(self.seq)):
            if self.seq[i] < self.s_smallest and self.seq[i] != self.smallest:
                self.s_smallest = self.seq[i]

        return self.s_smallest

def main():
    print("Application for find the secong smallest number in list")
    data = [13,56,89,9,23,65,45,32,10]

    obj = Classifier(data)
    ans = obj.Sec_Smallest()
    print("List is : ",data)
    print("Second smallest value in list is : ",ans)

if __name__ == "__main__":
    main()