# 4 Hirarchical inheritance(1 parent, many child)

# When multiple childs inherited by one parent class then its called hirarchical inheritance.


class Company:
    def __init__(self,name,city,country):
        self.name = name    
        self.city = city
        self.country = country
    def __str__(self):
        return f'Company name:{self.name}\t City:{self.city}\t Country:{self.country}'

class Product(Company):
    def __init__(self,name,price):
        self.name = name
        self.price = price
        super().__init__(input('Enter Company name:'),input('Enter city:'),input('Enter country:'))
    def __str__(self):
        print(super().__str__())
        return f'Product name:{self.name}\t Price:{self.price}'

class Employee(Company):
    def __init__(self,name,idno,post,salary):
        self.name = name
        self.idno = idno
        self.post = post
        self.salary = salary
        super().__init__(input('Enter Company name:'),input('Enter city:'),input('Enter country:'))
    def __str__(self):
        print(super().__str__())
        return f'Employee name:{self.name}\t Idno:{self.idno}\t Post:{self.post}\t Salary:{self.salary}'

class Labour(Company):
    def __init__(self,name,idno,salary):
        self.name = name
        self.idno = idno
        self.salary = salary
        super().__init__(input('Enter Company name:'),input('Enter city:'),input('Enter country:'))
    def __str__(self):
        print(super().__str__())
        return f'Name:{self.name}\t Idno:{self.idno:}\t Salary:{self.salary}'
#print(Labour.__mro__)
print('Enter your choice\nYour choice bellongs to your company')
print('1. Labour\n'
      '2. Employee\n'
      '3. Product\n'
      '4. Exit')

ch = int(input('Enter your choice:'))
for i in range(ch):
    if ch == 1:
        l = Labour(input('Enter labour name:'),int(input('Enter idno:')),input('Enter salary:'))
        print(l)
        break
    elif ch == 2:
        e = Employee(input('Enter employee name:'),int(input('Enter idno:')),input('Enter post:'),input('Enter salary:'))
        print(e)
        break
    elif ch == 3:
        p = Product(input('Enter product name:'),int(input('Enter price:')))
        print(p)
        break
    elif ch == 4:
        print('Exit')
        break
    else:
        print('Invalid choice')
        break
    
