# Write a program to check whether list is empty or not

# without using builtins 

class Classifier:
    def __init__(self,seq):
        self.seq = seq
        self.res = 0
        
    def Find(self):
        for i in self.seq:
            self.res += 1
        return self.res

def main():
    print("Find the list is empty or not without using built-in function")
    data = []
    obj = Classifier(data)
    ans = obj.Find()
    if ans == 0:
        print("Your list is empty")
    else:
        print("Your list is not empty")

if __name__ == "__main__":
    main()
