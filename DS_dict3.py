# Write a program to convert two list in dictionary

class Classifier:
    def __init__(self,seq1,seq2):
        self.seq1 = seq1
        self.seq2 = seq2
        self.res = dict()

    def ConvertDict(self):
        for i in range(len(self.seq1)):
            for j in range(len(self.seq2)):
                if i == j:
                    self.res[self.seq1[i]] = self.seq2[j]
        return self.res

def main():
    print("Application for convert two list into dictionay")
    l1 = ["one","two","three","four","five"]
    l2 = [1,2,3,4,5]

    obj = Classifier(l1,l2)
    ans = obj.ConvertDict()
    print("Converted dictionary : ",ans)


if __name__ == "__main__":
    main()
   
