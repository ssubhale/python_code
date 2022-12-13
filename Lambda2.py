# Using lambda function with Python built-ins

## filter

'''
The filter() function used to select some particular element from a sequence of a element

syntax-
result = filter(function, sequence)
-It return a filter object thats why we have typecast the filter function in required iterable like list, tuple and set
'''


def Program(ages):
    x = tuple(filter(lambda a : a > 50,ages))
    print(x)

def main():
    print("Application for demonstration of filter fn with lambda fn")
    ages = [23,12,53,83,56,52,87,56,34,68]
    Program(ages)

if __name__ == "__main__":
    main()
