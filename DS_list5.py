
#_1.Program to creat odd-even elements list from given list

class Classifier:
    def __init__(self,seq):
        self.seq = seq

    def CheckOddEven(self):
        odd,even = [], []
        for i in self.seq:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        return odd, even

def main():
    print("Application for separate list elements in odd even")
    data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

    obj = Classifier(data)
    ans1, ans2 = obj.CheckOddEven()
    print("odd list : ",ans1)
    print("even list : ",ans2)

if __name__ == "__main__":
    main()
