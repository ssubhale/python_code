# To reduce the code use for loop

class Student:
    def __init__(self,rn,nm,ad):
        self.rollno = rn
        self.name = nm
        self.address = ad

    def __str__(self):
        return f'Rollno:{self.rollno}\tName:{self.name}\tAddress:{self.address}\n'

n = int(input('Enter no of students:'))
for i in range(n):
    s = Student(int(input('Enter rollno:')),input('Enter name:'),input('Enter address:'))
    print(s)


class Customer:
    def __init__(self,cid,name,add):
        self.cid = cid
        self.name = name
        self.add = add

    def __str__(self):
        return f'Id:{self.cid}\tName:{self.name}\tAddress:{self.add}'

n = int(input('Enter no of customer :'))
for i in range(n):
    c = Customer(int(input('Enter customer id :')),input('Enter customer name :'),input('Enter customer address :'))
    print(c)