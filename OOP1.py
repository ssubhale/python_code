 ##__Object Oriented programing

#_It is a concept of designed and developed by some other person and its implimented in various programing languages.
#_one of the programming language is Python. This concept is desined on our day to day life Because of this concept,language 
# learning and understanding will be esier. In Python OOP is a programing paradigm that uses classes and objects in programing.


##Class :
#_A class is a collection of objects and class contain the blueprint or the prototype from which the objects are being created.
#_It is logical entity that contains some attributes and methods.

##Object :
# An object is simply a collection of data and methods that act on those data. Dimilarly, a class is a blueprint for that object.
#   Ex. Student, Teacher, Customer, Bikes, Cars

#self is variable which is used to hold the current object.It signifies that which object is calling the method.


#Ex.of class
class A:
    x = 15 #class variable
    def m1(self):  #method
        print('Jay Shriram')
        print(A.x)  #class_name.class_variable

a = A()  #object
a.x = 20 #instance variable
print(a.x)
a.m1()  #method call
a1 = A()#object
print(a1.x)
a1.m1()


class Student:  #class
    def display(self):  #method
        print('Roll no:',self.rollno)
        print('Name:',self.name)
        print('Address:',self.add)
        print('- - - - -')

s1 = Student()  #object
s1.rollno = 1
s1.name = 'abc'
s1.add = 'Pune'
s1.display()  #method call