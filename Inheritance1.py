##Inheritance
'''
_Inheritance means properties of one class can be inheritate by another class.There is parent child relationship between classes
_parent class is known as base class or super class, Child class is known as derived class or subclass
_allways child inherites the properties of parents, Object class is parent of all classes in Python
'''

#_super function is used to access the properties of imidiate parent

class A: #parent class
    x = 10
    def m1(self):
        print('m1 of A')

class B(A): #child class
    x = 20
    def m1(self):
        print('m1 of B')
        print(super().x)
        print(A.x)
        super().m1()
        A.m1(self)
b = B()  #object
print(b.x)
b.m1()