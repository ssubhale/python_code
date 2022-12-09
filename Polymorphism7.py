## Polymorphism

# MultipleDispatch
'''
multiple dispatch:
1.pip install multipledispatch
2.import into file then use
from multipledispatch import dispatch

It is used only in function and method overloading not on constructor
'''

from multipledispatch import dispatch
@dispatch(int,float)
def Add(a,b):
    print("int + float : ",a+b)


@dispatch(str,str)
def Add(a,b):
    print("str + str : ",a+b)

@dispatch(int,float,int)
def Add(a,b,c):
    print("int + float + int : ",a+b+c)


@dispatch(float,float)
def Add(a,b):
    print("float + float : ",a+b)


def main():
    print("Apllication for demonstration of multiple dispatch")
    Add(10,3.4)
    Add("Jay","Shriram")
    Add(4,6.3,9)
    Add(2.3,9.45)

if __name__ == "__main__":
    main()