
#_6.Given a list find a value of 10 from list and replace it with 100. must have 10 2 to3 itmes in list

class Classifier:
    def __init__(self,seq):
        self.seq = seq

    def Replace(self):
        for i in range(len(self.seq)):
            if self.seq[i] == 10:
                self.seq.pop(i)
                self.seq.insert(i,100)
        return self.seq

def main():
    print("Application for turn list element 10 into 100")
    data = [2,4,10,9,21,10,6,3,11,10,8,5]

    obj = Classifier(data)
    ans = obj.Replace()
    print("After replacing 10 into 100 : ",ans)

if __name__ == "__main__":
    main()