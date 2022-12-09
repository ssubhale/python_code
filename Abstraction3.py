
#_An abstract class which has only unimplemented abstract methods is known has interface.
#  Abstract class can have instance methods.
#   An Interface can only declare constants and instance methods, but cannot implement it.
#    method in abstract class. An interface has all public members and no implementation.


# Real life example of abstract class

from abc import ABC, abstractmethod

class RBI():
    @abstractmethod
    def interest_rate(self):  ## interface
        pass

    @abstractmethod
    def repo_rate(self):
        pass

class SBI(RBI):
    def interest_rate(self):
        print('Interest rate of SBI is 8%')

    def repo_rate(self):
        print('Repo  rate of SBI is 4%')

class HDFC(RBI):
    def interest_rate(self):
        print('Interest rate of HDFC is 7%')

    def repo_rate(self):
        print('Repo_rate of HDFC is 4%')

class ICICI(RBI):
    def interest_rate(self):
        print('Interest rate of ICICI is 9%')

    def repo_rate(self):
        print('Repo_rate of ICICI is 5%')

def main():
    print("Application for demonstration of abstraction")
    s = SBI()  #object
    s.interest_rate()
    s.repo_rate()
    h = HDFC()  #object
    h.interest_rate()
    h.repo_rate()
    i =ICICI()  #object
    i.interest_rate()
    i.repo_rate()

if __name__ == "__main__":
    main()

