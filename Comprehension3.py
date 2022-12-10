
## Dictionary comprehension

# Syntax:
# op_dict = {key:value for (key, value) in iterable if condition}


class Program:
    def __init__(self,seq):
        self.seq = seq

    def Square(self):
        sqr = {i:i*i for i in self.seq}
        return sqr

    def Cube(self):
        cub = {i:i**i for i in self.seq}
        return cub
        

def main():
    print("Application for demonstration of dictionary comprehension")
    data = [1,2,3,4,5,6]
    obj = Program(data)
    ans1 = obj.Square()
    print("List elements are keys and their values are square : ",ans1)

    ans2 = obj.Cube()
    print("List elements are keys and their values are cubes : ",ans2)

if __name__ == "__main__":
    main()