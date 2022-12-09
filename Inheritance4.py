## 3.Multiple inheritance(many parent, 1 child)

#_When a child class inherites from multiple parent classes, it is called multiple inheritance

class Father:
    def __init__(self,name,sirname,address):
        self.fname = name
        self.sirname = sirname
        self.address = address
        super().__init__(input('Enter Mother Name: '))

    def __str__(self):
        
        return f'Father name:{self.fname},\tSirname:{self.sirname:}, Address:{self.address}, {super().__str__()}'

class Mother:
    def __init__(self,name):
        self.mname = name
    def __str__(self):
        return f'Mother name:{self.mname}'

class Child(Father,Mother):
    def __init__(self,name,age,education):
        self.name = name
        self.age = age
        self.education = education
        super().__init__(input('Enter father name: '),input('Enter sirname: '),input('Enter address: '))
                
    def __str__(self):
        print(super().__str__())
        return f'Name:{self.name}, \tAge:{self.age}, \tEducation:{self.education}'


def main():
    print("Application for demonstration of multiple inheritance")
    num = int(input("Enter no of child : "))
    for i in range(num):
        c = Child(input('Enter name:'),input('Enter age:'),input('Enter education:'))
        print(c)

if __name__ == "__main__":
    main()


    