
#_2.Program to creat positive-negative elements lists from given list

class Classifier:
    def __init__(self,seq):
        self.seq = seq

    def PositiveNegative(self):
        pos,neg = [], []
        for i in self.seq:
            if i > 0:
                pos.append(i)
            else:
                neg.append(i)

        return neg, pos

def main():
    print("Application for separate list elements in positive or negative")
    data = [1,-2,-3,2,9,4,5,6,-7,8,-9,10,11,-12,13,-14,15,16]

    obj = Classifier(data)
    ans1, ans2 = obj.PositiveNegative()
    print("Positive elements : ",ans1)
    print("Negative elements : ",ans2)

if __name__ == "__main__":
    main()
