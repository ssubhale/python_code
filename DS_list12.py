#_8.Remove completely the 5's from list


class Classifier:
    def __init__(self,seq,no):
        self.seq = seq
        self.no = no

    def Remove(self):
        while 5 in self.seq:
            self.seq.remove(5)
        return self.seq

def main():
    print("Application for remove the completely 5 from list")
    data = [1,5,5,6,7,5,5,2,7,8,5,5,9,5,4,5]
    no = 5
    print('Original list : ',data)
    obj = Classifier(data,no)
    ans = obj.Remove()
    print("list after removing 5 : ",ans)

if __name__ == "__main__":
    main()