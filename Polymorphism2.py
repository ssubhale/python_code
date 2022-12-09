## Polymorphism

# Overloadnig

## 2 Method overloading 

# with default argument
class A:
    def Add(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            print(a+b+c)
        elif a != None and b != None:
            print(a+b)
        elif a != None:
            print(a)
        else:
            print(0)

# with veriable length argument
class B:
    def Add(self,*args):
        sum = 0
        for i in args:
            sum += i
        print(sum)

def main():
    print("Method overloadiing with default arguments")
    a = A()
    a.Add()
    a.Add(12)
    a.Add(12,14)
    a.Add(12,14,16)
    # a.Add(12,14,16,18) # TypeError: Add() takes from 1 to 4 positional arguments but 5 were given

    print("Method with veriable length argument")
    b = B()
    b.Add()
    b.Add(12,14)
    b.Add(12,14,16)
    b.Add(12,14,16,18)

if __name__ == "__main__":
    main()