## 4. Polymorphism

#_It means having many forms In python, polymorphism means same function name but different working
#_We achive polymorphism by overloading, overriding and ducktyping

# 1. Overloading

## Overloading is the process where same function or method can be used multiple
## times by passing the different number of parameters as arguments.

#_ it means same name having diffrent forms.
#_Python does not support traditional overloading rather it gives a different way for it.
#_Overloading is achived by default argument and variable length argument, or multiple dispatch
#_we can overload function, method, constructor and operator.


## Function overloading

# 1. with default argument

def Add(a=None, b=None, c=None):
    if a != None and b != None and c != None:
        print(a+b+c)

    elif a != None and b != None:
        print(a+b)

    elif a != None:
        print(a)

    else:
        print("No arguments specified")


# 2. with veriable length arguments
def Addition(*args):
    a = 0
    for i in args:
        a += i
    print(a)


def main():
    print("Function overloading with default arguments")
    Add()
    Add(12,14)
    Add(12,14,16)
    # Add(12,14,16,18) #TypeError: add() takes from 0 to 3 positional arguments but 4 were given
    '''
       In default arguments, there is one drawback that we can give at most that many arguments which 
       we have defined as default in function definition. So last function call will generate error. 
       We can overcome this drawback in variable length arguments.
    '''
    print("Function overloading with variable length arguments")
    Addition()
    Addition(12,14)
    Addition(12,14,16)
    Addition(12,14,16,18)
    Addition(12,14,16,18,20)

if __name__ == "__main__":
    main()