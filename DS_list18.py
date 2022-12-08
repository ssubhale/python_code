# Write a program to find the largest element in list

class Classifier:
    def __init__(self,seq):
        self.seq = seq
        self.largest = 0

    def Largest(self):
        self.largest = self.seq[0]
        for i in range(len(self.seq)):
            if self.seq[i] > self.largest:
                self.largest = self.seq[i]
        return self.largest

def main():
    print("Application for find the largest value in list")
    data = [23,53,12,38,29,10,30,22,54,90,43]

    obj = Classifier(data)
    ans = obj.Largest()
    print("List is : ",data)
    print("Largest number in list is : ",ans)

if __name__ == "__main__":
    main()