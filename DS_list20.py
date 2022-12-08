# Write a program to find smallest value in list

class Classifier:
    def __init__(self,seq):
        self.seq = seq
        self.smallest = 0

    def Smallest(self):
        self.smallest = self.seq[0]
        for i in range(len(self.seq)):
            if self.seq[i] < self.smallest:
                self.smallest = self.seq[i]
        return self.smallest

def main():
    print("Application for find the smallest number in list")
    data = [4,21,8,56,70,45,93,23,2,10]
    obj = Classifier(data)
    ans = obj.Smallest()
    print("List is : ",data)
    print("Smallest number in list is : ",ans)

if __name__ == "__main__":
    main()
