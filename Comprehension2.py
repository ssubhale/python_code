## Set comprehension

#   Set comprehensions are pretty similar to list comprehensions. The only 
# difference between them is that set comprehensions use curly brackets {}.

# Syntax
# output_set = {output_var for var in input_set if condition}

class Program:
    def __init__(self,seq):
        self.seq = seq

    def OddSet(self):
        odd = {i for i in self.seq if i%2 != 0}
        return odd

    def Square(self):
        sqr = {i*i for i in range(1,21) if i%2 == 0}
        return sqr


def main():
    print("Application for demonstration of set comprehension")
    data = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}

    obj = Program(data)
    ans1 = obj.OddSet()
    print("Set of odd elements from existing set : ",ans1)

    ans2 = obj.Square()
    print("Set of square elements from range in 20 : ",ans2)

if __name__ == "__main__":
    main()