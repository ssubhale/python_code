# Write a program to remove the duplicate from list.


class Classifier:
    def __init__(self,seq):
        self.seq1 = seq
        self.seq2 = list()

    def RemoveDups(self):
        for i in self.seq1:
            if i not in self.seq2:
                self.seq2.append(i)
        return self.seq2


def main():
    print("Application for remove the duplicate from list")
    data = [4,4,6,8,6,4,4,2,12,8,0,9,0,6,5,4]

    obj = Classifier(data)
    ans = obj.RemoveDups()
    print("Original list : ",data)
    print("List after removing duplicates : ",ans)

if __name__ == "__main__":
    main()
