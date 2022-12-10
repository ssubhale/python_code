#  Its project on student information about insert data and display data

class Student:
    def setRollno(self,rn):
        self.__rn = rn

    def getRollno(self):
        return self.__rn

    def setName(self,nm):
        self.__nm = nm

    def getName(self):
        return self.__nm

stu = list()

def main():
    print("Application for demonstration of student record")
    print("     1. Insert data \n     2. Display data \n     3. Exit from application")

    while True:
        ch = int(input("Enter your operation code : "))
        if ch == 1:
            n = int(input("Enter no. of student you want to insert data : "))
            for i in range(n):
                s = Student()
                s.setRollno(int(input("Enter roll no. : ")))
                s.setName(input("Enter name : "))
                stu.append(s)
        elif ch == 2:
            if len(stu) != 0:
                print("---------- Display Menu ----------")
                print("1. Display all records \n2. Display specific record \n3. Exit from display data ")
                while True:
                    ch1 = int(input("Enter your choice for display menu : "))
                    if ch1 == 1:
                        print("---------- Student Records ----------")
                        for i in stu:
                            print("Rollno : ",i.getRollno())
                            print("Name : ",i.getName().lower())

                    elif ch1 == 2:
                        par = input("Enter parameter(Rollno/Name) : ")
                        if par.lower() == "rollno":
                            rn = int(input("Enter rollno to search : "))
                            for i in stu:
                                if i.getRollno() == rn:
                                    print("Rollno : ",i.getRollno())
                                    print("Name : ",i.getName())
                                    break
                                else:
                                    print("Record not exists for this rollno")
                                    break
                        elif par.lower() == "name":
                            nm = input("Enter name to search : ")
                            for i in stu:
                                if i.getName() == nm:
                                    print("Rollno : ",i.getRollno())
                                    print("Name : ",i.getName())
                                    break
                                else:
                                    print("Record not found for this name")
                                    break
                        else:
                            print("You entered wrong parameter")

                    else:
                        print("Exit from display menu ")
                        break
            else:
                print("Record not found for display ")

        elif ch == 3:
            print("Exit from application")
            exit()

        else:
            print("You enterd wrong choice for application")


if __name__ == "__main__":
    main()