# input list is 
l1 = [1,2,3,4,"krishna"]

# output list is
l2 = [5,10,15,20,"Shrikrishna"]


# with using for loop
# with using ternery operator

class Classifier:
    def __init__(self,seq):
        self.seq1 = seq
        self.seq2 = list()

    def ForLoop(self):
        for i in self.seq1:
            if i == str:
                i = "Shri" + i
            else:
                i * 5
        return self.seq1

    def Ternary(self):
        self.seq2 = ['Shri'+i if type(i) == str else i*5 for i in self.seq1]
        return self.seq2

def main():
    data = [1,2,3,4,"krishna"]

    obj = Classifier(data)
    ans1 = obj.ForLoop()
    print("Anser by for loop : ",ans1)

    ans2 = obj.Ternary()
    print("Answer by ternary operator : ",ans2)


if __name__ == "__main__":
    main()