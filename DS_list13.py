#_9.Find the transpose of matrix

class Classifier:
    def __init__(self,seq):
        self.seq = seq
        

    def Transpose(self):
        self.transpose = []
        for i in range(len(self.seq[0])):
            self.trans = []
            for j in self.seq:
                self.trans.append(j[i])
            self.transpose.append(self.trans)
        return self.transpose


def main():
    print("Application for to find the transpose of matrix")
    data = [[10,20,30,40],[50,60,70,80]]
    # ountput = [[10, 50], [20, 60], [30, 70], [40, 80]]

    obj = Classifier(data)
    ans = obj.Transpose()
    print("Original nested list : ",data)
    print("Transpose of matrix : ",ans)

if __name__ == "__main__":
    main()
