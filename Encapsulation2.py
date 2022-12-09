##_Access the private var or method by setter_getter method

class Student:
    def setRollno(self,rollno): ##initialize the variable
        self.__rollno = rollno
    def getRollno(self): ##access the var
        return self.__rollno

    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name

def main():
    print("Application for demonstration of encapsulation with setter-getter")
    s = Student()
    s.setRollno(12)
    s.setName('Karan')
    s1 = Student()
    s1.setRollno(10)
    s1.setName('Ram')
    print('Rollno:',s.getRollno())
    print('Name:',s.getName())
    print('Rollno:',s1.getRollno())
    print('Name:',s1.getName())
    
if __name__ == "__main__":
    main()
