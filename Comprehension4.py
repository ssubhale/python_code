##.4 Generator Comprehensions

#   Generator Comprehensions are very similar to list comprehensions. One difference between them is that generator comprehensions 
# use circular brackets whereas list comprehensions use square brackets. The major difference between them is that generators don’t 
# allocate memory for the whole list. Instead, they generate each value one by one which is why they are memory efficient.

#Syntax:
#   output_gen = (var for var in input_sequence if condition)


class Program:
    def __init__(self,seq):
        self.seq = seq

    def Even(self):
        even = (i for i in self.seq if i%2 == 0)
        return even
        

def main():
    print("Application for demonstration of generator comprehension")
    data = [42,15,9,10,29,3,4,5,6,7,12,54,67,13]

    obj = Program(data)
    ans = obj.Even()
    for i in ans:
        print(i,end=" ")

if __name__ == "__main__":
    main()