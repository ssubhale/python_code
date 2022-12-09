## Polymorphism

## Duck typing
#_provide a common interface for similer method.

#   It means providing a common interface to call the methods of different classes, If the methods have same name. 
# We can create polymorphism with a function that can take any object as a parameter and execute its method without checking its class type. 
# Using this, we can call object actions using the same function instead of repeating method calls.


class Balloon:
    def Fly(self):
        print("Balloons fly with the help of air")


class Aeroplane:
    def Fly(self):
        print("Aeroplane fly with the help of fuel")


class Bird:
    def Fly(self):
        print("Birds fly with the help of wings")

def Common(obj):
    obj.Fly()

def main():
    print("Application for demonstration of ducktyping")

    ## 1st way
    Common(Balloon())
    Common(Aeroplane())
    Common(Bird())

    ## 2nd way
    meth = [Balloon(),Aeroplane(),Bird()]
    for i in meth:
        Common(i)

    ## 3rd way
    for i in Balloon(),Aeroplane(),Bird():
        Common(i)

if __name__ == "__main__":
    main()