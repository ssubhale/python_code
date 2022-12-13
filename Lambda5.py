## Lambda function with filter(), map() and reduce()

def CheckEven(no):
    return (no % 2 == 0)

def Square(no):
    return no * no

def sum(a,b):
    return a + b

def filterx(Helper_fun,data):
    result = []
    for no in data:
        if (Helper_fun(no) == True):
            result.append(no)

    return result

def mapx(Helper_fun,data):
    result = []
    for i in data:
        value = Helper_fun(i)
        result.append(value)

    return result

def reducex(Helper_fun,data):
    ans = 0
    for no in data:
        ans = Helper_fun(ans,no)

    return ans

def main():
    print("Application for demonstration of lambda fn with user defined filter,map,reduce")
    
    isize = int(input("Enter no. of elements you want to add in list : "))
    data = []

    for i in range(isize):
        value = int(input("Enter value : "))
        data.append(value)

    print("You enterd list is : ",data)

    # find even numbers from list by user defined filter function
    data_filter = filterx(CheckEven,data)
    print("Data after filter : ",data_filter)

    # find square of each element by user defined map function
    data_map = mapx(Square,data_filter)
    print("Data after map is : ",data_map)

    # find sum of all elements by user defined reduce function
    output = reducex(sum,data_map)
    print("Result after reuce is : ",output)

if __name__ == "__main__":
    main()