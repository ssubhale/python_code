## Deep copy
'''
-In simple as well as in nested structure changes made in original are not reflected in new because there is separate memmory 
address are assigned for nested structure
'''
def DeepCopy():

    l1 = [1,2,3]
    l2 = [4,5,6]
    l3 = [l1,l2]
    print(l3)

    import copy
    l4 = copy.deepcopy(l3)
    print(l4)

    l1.append(10)
    print(l1)
    print(l3)
    print(l4)

    print(id(l1))
    print(id(l3))
    print(id(l4))

def main():
    print("Demonstration of deep copy in python")
    DeepCopy()

if __name__ == "__main__":
    main()

