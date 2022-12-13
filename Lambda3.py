##  map
'''
-The map() function is used to apply a particular operation to every element in a sequence

Syntax-
result = map(lambda_fn, sequence)

-The built-in function map() takes a lambda_fn as first argument and applies it to each of the elements of its second argument an iterable.
-It return a map object thats why we have typecast the map function in required iterable like list, tuple and set.
'''

#Ex.print the square of each element in the given list
def Program(l):
    sqr = list(map(lambda x : x ** 2, l))
    print(sqr)


def main():
    print("Application for demonstration for map fn with lambda fn")
    data = [1,2,3,4,5,6]
    Program(data)

if __name__ == "__main__":
    main()
