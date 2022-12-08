
#_5.program to turn every elelment of list into square

class Classifier:
    def __init__(self,seq):
        self.seq = seq

    def Square(self):
        sqr = []
        for i in self.seq:
            sqr.append(i*i)
        return sqr

def main():
    print("Application for turn every element into square in list")
    data = [4,3,7,9,8,5,3,0]

    obj = Classifier(data)
    ans = obj.Square()
    print("Original list is : ",data)
    print("List after turning every element in square : ",ans)

if __name__ == "__main__":
    main()