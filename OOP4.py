
#Object of one class is refered by another class

class Address:
    def __init__(self,city,area):
        self.city = city
        self.area = area

    def __str__(self):
        return f'City:{self.city}\tArea:{self.area}'

class Student:
    def __init__(self,rollno,name,adr):
        self.rollno = rollno
        self.name = name
        self.adr = adr

    def __str__(self):
        return f'Roll no:{self.rollno}\tName :{self.name}\nAddress :\t{self.adr}'

a1 = Address('Pune','Akurdi')
a2 = Address('Mumbai','Andheri')
a3 = Address('Nashik','Nimani')

s1 = Student(1,'Krishna',a1)
s2 = Student(2,'Ram',a2)
s3 = Student(3,'Sagar',a3)

print(s1)
print(s2)