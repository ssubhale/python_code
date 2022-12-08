# Write the program to find the second largest value in list

class Classifier:
    def __init__(self,seq):
        self.seq = seq
        self.largest = 0
        self.s_largest = 0

    def Sec_largest(self):
        self.largest = self.seq[0]
        self.s_largest = self.seq[0]

        for i in range(len(self.seq)):
            if self.seq[i] > self.largest:
                self.largest = self.seq[i]

        for i in range(len(self.seq)):
            if self.seq[i] > self.s_largest and self.seq[i] != self.largest:
                self.s_largest = self.seq[i]

        return self.s_largest

def main():
    print("Application for find second largest values from list")
    data = [45,67,3,5,9,8,60,43,32,65,61,3,9,0,31]

    obj = Classifier(data)
    ans = obj.Sec_largest()
    print("Second largest value in list is : ",ans)

if __name__ == "__main__":
    main()
