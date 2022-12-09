## Abstraction

#_abstraction means hiding the complex structure and only essential features are shown to user.
#_abstraction is achive through abstract class.
#_abstract is class which is inherite from ABC class and it must contain atleast
#   one abstractmethod which is decorated by abstract method decorator.
#_we get the ABC class and decorator from abc module.


## syntax
'''
from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def m1(self):
        pass
'''
# To access the abstract class we cannot create the object of it, To access it,we have
# _to create child class of abstract class
# The child class must be implemented all the abstract method of abstract class.
# If child fetch to implement any abstractmethod then child class also become abstract class.

#Ex
from abc import ABC, abstractmethod
class P(ABC):
    @abstractmethod
    def m1(self):   #unimplemented method
        pass

    @abstractmethod
    def m2(self):   #implemented
        print('m2 of P')

    def m3(self):
        print('m3 of P')
        
class Q(P):
    def m1(self):
        print('m1 of Q')
        super().m1()
        
    def m2(self):   
        print('m2 of Q')
        super().m2()

def main():
    q = Q()
    q.m1()
    q.m2()

if __name__ == "__main__":
    main()
