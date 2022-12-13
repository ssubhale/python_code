## Reduce    
'''
-Since, Python 3.0, reduce() function has gone from a built-in function to a functools module function

syntax-
result = reduce(function, sequence)
-When we do some operations of an iterables and the resulted output is just a single value then we used 
reduce() function, Thats why reduce() function no need to typecast into any other data structure.
'''
from functools import reduce

#Ex.find the sum of all element in the given list

def Program(m):
    res = reduce(lambda a, b : a + b, m)
    print(res)


def main():
    print("Application for demonstration of reduce fn with lambda fn")
    marks = [56,68,94,63,78,59]
    Program(marks)

if __name__ == "__main__":
    main()