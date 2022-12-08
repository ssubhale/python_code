
##Class and objects in sets


class Student:
    def __init__(self,rn,nm,addr):
        self.rollno = rn
        self.name = nm
        self.addr = addr

    def __str__(self):
        return f'Rollno:{self.rollno}\tName:{self.name}\tAddr:{self.addr}\n'
def main():
    s1 = Student(1,'abc','Pune')
    s2 = Student(2,'xyz','Mumbai')
    s3 = Student(3,'pqr','Nashik')
    s4 = Student(4,'mno','Jalgaon')  ##student

    mca1 = {s1,s2}  ##division
    mca2 = {s3,s4}

    ## Convert in frozenset

    fmca1 = frozenset(mca1)
    fmca2 = frozenset(mca2)

    mca = set()

    mca.add(fmca1)
    mca.add(fmca2)

    for i in mca:
        for j in i:
            print(j)

if __name__ == "__main__":
    main()