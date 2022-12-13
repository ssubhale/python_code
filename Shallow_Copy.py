
## Shallow copy

#   -Shallow copy on simple structure acts likes cloning.In nested structure changes made in original nested structure are reflected in copied structure. 
#    because memmory address are stored in nested structure. copy module is used for shallow copy.

import copy


def  Simple():
    print("Shallow copy in simple structure")
    l1 = [10,20,30]
    l2 = copy.copy(l1) # .copy() ---> function
    print(l1)
    print(l2)
    print(id(l1))
    print(id(l2)) # It will be different not same
    l1.append(40) # append element only in l1
    print(l1)
    print(l2)


def Nested():
    print("Shallow copy for nested structure")
    m1 = [10,20,30]
    m2 = [40,50,60]

    m3 = [m1,m2]
    print(m3)
    print('m3',id(m3))

    m4 = copy.copy(m3)
    print(m4)
    print('m4',id(m4))

    m1.append(35)
    print(m3)
    print(m4)

    m3.append(100)
    print(m3)
    print(m4)

def main():
    print("Demonstration of shallow in python")
    Simple()
    Nested()

if __name__ == "__main__":
    main()