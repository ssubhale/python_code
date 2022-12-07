
## str method in python

#string representation of an object and it called automatically when we print object, If str is not present in class 
# then memmory address is printed. It allways return strings



#Ex.1
class Student:
    def __init__(self,rn,nm,mks):  #constructor
        self.rollno =rn
        self.name = nm
        self.marks = mks

    def __str__(self):  #string
        return'Roll no:{}\tName:{}\tMarks:{}\n'.format(self.rollno, self.name, self.marks)

s1 = Student(1,'abc',75.9)  #object
print(s1)
s2 = Student(1,'xyz',78.5)
print(s2)

#Ex.2
class Employee:
    def __init__(self,idno,nm,post):
        self.idno = idno
        self.name = nm
        self.post = post

    def __str__(self):
        return f'Id no:{self.idno}\tName:{self.name}\tPost:{self.post}\n'
        
e1 = Employee(10,'abc','manager')
print(e1)
e2 = Employee(11,'xyz','hod')
print(e2)


