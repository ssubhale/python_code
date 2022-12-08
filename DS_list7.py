
#_3.Program to count elements in a list without using len()function

class Classifier:
    def __init__(self,seq):
        self.seq = seq

    def CountElements(self):
        count = 0
        for i in self.seq:
            count += 1
        return count

def main():
    print("Application for count the elements from list without using built-ins")
    data = [1,3,5,3,2,1,6,7,8,5,9,8]

    obj = Classifier(data)
    ans =obj.CountElements()
    print("Count of list is : ",ans)

if __name__ == "__main__":
    main()