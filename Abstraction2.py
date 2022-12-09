## Example of Abstraction 

from abc import ABC, abstractmethod 
class Car(ABC):
    @abstractmethod
    def milage(self):
        pass

    @abstractmethod
    def transmission(self):
        pass

class Nexon(Car):
    def milage(self):
        print("Milage is 15kmpl")

    def transmission(self):
        print("Transmision is 6AT")

class Suzuki(Car):
    def milage(self):
        print("Milage is 18kmpl")

    def transmission(self):
        print("Transmision is 9AT")

class Jeep(Car):
    def milage(self):
        print("Milage is 16kmpl")

    def transmission(self):
        print("Transmision is 6MT")

class Duster(Car):
    def milage(self):
        print("Milage is 16kmpl")

    def transmission(self):
        print("Transmision is 9AT")

def main():
    print("Application for demonstration of abstraction")

    n =Nexon()
    n.milage()
    n.transmission()

    s = Suzuki() 
    s.milage()
    s.transmission()

    d = Duster() 
    d.milage()
    d.transmission()

    j = Jeep()
    j.milage()
    j.transmission()

if __name__ == "__main__":
    main()
