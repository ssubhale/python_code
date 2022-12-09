## Indirect subclass
# indirect subclass is created by registering it through parent class by register method.
# the properties of direct subclass is not valid for indirect subclass.
# so when we do not want to implement all abstract method in direct subclass we use indirect subclass.
## _Register method is registered only for abstractclass -->(.register())

#EX.

from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass

    def m3(self):
        print('m3 of A')

class B(A):  #direct subclass
    def m1(self):
        print('m4 of B')

    def m2(self):
        print('m5 of B')
        super().m3()

class C:  #indirect subclass
    def m1(self):
        print('m1 of C')

    def m2(self):
        print('m2 of C')

def main():

    b = B()
    b.m1()
    b.m2()

    print('Before registering:',issubclass(C,A))

    A.register(C)  #register method

    print('After registering:',issubclass(C,A))

    c = C()
    c.m1()
    c.m2()

    print('Name of direct subclass')     
    for subclass in A.__subclasses__():  # it return the list of immediat
        print(subclass.__name__)  #  subclass of parent.

if __name__ == "__main__":
    main()