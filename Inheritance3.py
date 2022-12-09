## 2.Multi-level inheritance(1 parent, 1 child ,1 grand child)

#_Its achived when a child class inherites from another child class, here is no limit on the no of levels.

class University:
    def __init__(self,U_name):
        self.U_Name = U_name


class College(University):
    def __init__(self,C_name):
        self.C_Name = C_name
        super().__init__(input('Enter university name :'))

    
class Student(College):
    def __init__(self,nm,deg,yr):
        self.Name = nm
        self.Degree = deg
        self.Year = yr
        super().__init__(input("Enter college name : "))

    def __str__(self):
        return f"Student name : {self.Name}\nDegree : {self.Year}\nYear : {self.Year}\nCollege : {self.C_Name}\nUniversity : {self.U_Name}"

def main():
    print("Application for multi-level inheritance")
    obj = Student(input("Enter student name : "),input("Enter student degree : "),int(input("Enter year : ")))
    print(obj)

if __name__ == "__main__":
    main()