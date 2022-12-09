## Polymorphism

# Overloading

# Constructor overloading

# with default argument
class A:
    def __init__(self,a=None, b=None, c=None):
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
    def __init__(self,*args):
        sum = 0
        for i in args:
            sum += i
        print(sum)

def main():
    print("Constructor overloading with default argument")
    a = A()
    a1 = A(12)
    a2 = A(12,14)
    a3 = A(12,14,16)
    # a4 = A(12,14,16,18) # TypeError: __init__() takes from 1 to 4 positional arguments but 5 were given

    print("Constructor overloading with variable length argument")
    b = B()
    b1 = B(12)
    b2 = B(12,14)
    b3 = B(12,14,16)
    b4 = B(12,14,16,18)
    b5 = B(12,14,16,18,20)

if __name__ == "__main__":
    main()
