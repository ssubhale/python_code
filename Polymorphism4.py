## Polymorphism

# Operator overloading

#   Operator overloading means changing the default behaviour of an operator depending on the operands (values) that we use.
# In other words, we can use the same operator for multiple purposes.

#Ex. Overload the + operator with magic method __add__()


class Book:
    def __init__(self, pages):
        self.pages = pages
      
    def __add__(self, other):
        total = self.pages + other.pages
        return Book(total)

    def __str__(self):
        return f"{self.pages}"

def main():
    b1 = Book(400)
    b2 = Book(300)
    b3 = Book(250)
    b4 = Book(300)
    print("Total number of pages: ", b1 + b2 + b3 + b4)

if __name__ == "__main__":
    main()