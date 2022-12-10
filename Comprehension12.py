# Find the given output from foloowing list by list comprehension

Input = [[1, 2, 3], [4, 5], [6, 7, 8, 9]] 
Output = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def Program(seq):
    l = [j for i in seq for j in i]
    return l

def main():
    print("Application for demonstration of list comprehension")
    data = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    ans = Program(data)
    print("Output list : ",ans) 


if __name__ == "__main__":
    main()