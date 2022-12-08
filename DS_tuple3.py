# Sort a tuple of tuples by 2nd items

t = (('a',23),('b',37),('c',11),('d',29))


class Student:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

def main():
    print("Application for sort the tuple of tuples by second item")
    
    s1 = Student("a",23)
    s2 = Student("b",37)
    s3 = Student("c",12)
    s4 = Student("d",56)
    s5 = Student("e",45)

    l = [s1,s2,s3,s4,s5]

    l.sort(key = lambda i:i.y, reverse=True)
    for i in l:
        print(i)

if __name__ == "__main__":
    main()