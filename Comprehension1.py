## Comprehension

#   Comprehensions in Python provide us with a short and concise way to
# construct new sequences using sequences which have been already defined. 

## 1.List Comprehensions


#   List Comprehensions provide an elegant way to create new lists.
#   Note: in list comprehension only if and else support

# One of the most distinctive aspects of the python is the list and the list compression. 
# List comprehension can use within a single line of code to construct powerful functionality.

#Syntax:
#   output_list =[output_var for var in input_list if condition]

class Program:
    def __init__(self,seq):
        self.seq = seq
    
    def Square(self):
        sqr = [i*i for i in self.seq]
        return sqr

    def Cube(self):
        cb = [i**i for i in self.seq]
        return cb

    def EvenSquare(self):
        esqr = [i*i for i in range(21) if i%2 == 0]
        return esqr

    def OddCube(self):
        oddcub = [i**i for i in range(1,15) if i%2 != 0]
        return oddcub


def main():
    print("Application for demonstration of list comprehension")
    data = [1,2,3,4,5,6,7,8,9,10]
    obj = Program(data)
    ans1 = obj.Square()
    print("List converted every element in square : ",ans1)

    ans2 = obj.Cube()
    print("List converted every element in cube : ",ans2)

    ans3 = obj.EvenSquare()
    print("Converted even element into square in range of 20 : ",ans3)

    ans4 = obj.OddCube()
    print("Converted odd element into cube in range of 15 : ",ans4)

if __name__ == "__main__":
    main()