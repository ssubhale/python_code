## Encapsulation

# _It means wrapping the diffrent entity into a single entity, Encapsulation is achived by making the members as public, protected and private
# _best example of encapsuation is a class

##Members

#1 Public - it is accessed globaly
#ex.   x = 10

#2 Protected - it is like public only but it tells the developer do not change the value of it
#ex.   _y = 20

#3 Private - we can`t access private member by using object or class name, we access the private var or method by using name mangaling
#ex.   __z = 30

class A:
    x = 10
    _y = 20
    __z = 30
    
    def m1(self):
        print('Public method')

    def _m2(self):
        print('Protected method')

    def __m3(self):
        print('Private method')

def main():
    print("Application fro demonstration of Encpsulation")

    a = A()
    print(a.x)
    print(a._y)
    # print(a.__z) # We cannot access the private member by claname or object of class

    a.m1()
    a._m2()
    # a.m3() # We cannot access the private member by claname or object of class

    print("To access the private memers we have to use name mangelling")

    print("Private variable : ",a._A__z)
    a._A__m3()

if __name__ == "__main__":
    main()