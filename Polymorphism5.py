## Polymorphism

# Overriding

#   Polymorphism is mainly used with inheritance. In inheritance, child class inherits the attributes and methods of a parent class. 
# The existing class is called a base class or parent class, and the new class is called a subclass or child class or derived class.

## method overriding
#   Using method overriding polymorphism allows us to defines methods in the child class that have the same name as the methods in the parent class. 
# The process of re-implementing the inherited method in the child class is known as Method Overriding.

class Vehicle:
    def __init__(self,name,color,price):
        self.name = name
        self.color = color
        self.price = price

    def Show(self):
        print(f"Details ==>> Car name : {self.name} Color : {self.color} Price : {self.price}")

    def MaxSpeed(self):
        print("Vehicle max speed is 150kmph")

    def Milage(self):
        print("Milage is 16kmpl")

class Car(Vehicle):
    def MaxSpeed(self):
        print("Car max speed is 200kmph")

    def Milage(self):
        print("Milage is 15kmpl")

def main():
    print("Application for method overriding")
    c = Car("Nexon", "Red", "20,00,000")
    c.Show()
    c.MaxSpeed()
    c.Milage()


if __name__ == "__main__":
    main()