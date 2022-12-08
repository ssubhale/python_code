
#_7.Program to convert cdegree into fdegree

class Classifier:
    def __init__(self,cd):
        self.cdegree = cd
        self.fdegree = []        

    def Display(self):
        for i in self.cdegree:
            t = (9.0/5) * i + 32
            self.fdegree.append(t)
        print("\tCdegree\t\tFdegree")
        for i in range(len(self.cdegree)):
            print("\t",self.cdegree[i], "\t\t", self.fdegree[i])

def main():
    print("Application for to converet cdegree into fdegree")
    data = [20,30,45,56,61,73]

    obj = Classifier(data)
    obj.Display()

if __name__ == "__main__":
    main()