# Write a program to check whether list is empty or not

# Using builtins 

class Classifier:
    def __init__(self,seq):
        self.seq = seq
        
    def Find(self):
        flag = False
        if len(self.seq) == 0:
            flag = True
        else:
            flag = False
        return flag

def main():
    print("Find the list is empty or not using built-in function")
    data = [3,2,4,5,8]
    obj = Classifier(data)
    ans = obj.Find()
    if ans == True:
        print("Your list is empty")
    else:
        print("Your list is not empty")

if __name__ == "__main__":
    main()
