##Constructor in class

#_Constructor is denoted by a magic method named as __init__( ), It is called automatically when we creat object of a class.
#_It used to initialize the instance variable.

class A:
    def __init__(self): 
        print('Jay Shriram')
        
a1 = A( )
a2 = A( )

class B:
    def __init__(self):
        print('Jay Ganesh')
a3 = B()


class Student:
    def __init__(self,rn,nm,mks):  #constructor
        self.rollno = rn
        self.name = nm
        self.marks = mks

    def info(self):  #method
        print('Roll no:',self.rollno)
        print('Name:',self.name)
        print('Marks:',self.marks)


s1 = Student(11,'abc',78.5)  #object
s1.info( )  #method call

s2 = Student(12,'xyz',75.5)  #object
s2.info( )  #method call

s3 = Student(13,'pqr',73.5)  #object
s3.info( )  #method call
