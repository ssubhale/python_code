## 1.Single-level inheritance(1 parent 1 child)

#_when one child class inherites from only one parent class, it is called single level inheritance.
##  super()function is used to give acces to methods and properties of imidiate parent

class Address:
    def __init__(self,city,area):
        self.city = city
        self.area = area
    def __str__(self):
        pass

class Student(Address):
    def __init__(self,rn,nm):
        self.rollno = rn
        self.name = nm
        super().__init__(input('Enter city:'),input('Enter area:'))
    def __str__(self):
        #print(super().__str__())
        return f'Rollno:{self.rollno}\tName:{self.name}\nCity:{self.city}\t\tArea:{self.area}'

def main():
    n = int(input('Enter no of student:'))
    for i in range(n):
        s = Student(int(input('Enter rollno:')),input('Enter name:'))
        print(s)

if __name__ == "__main__":
    main()