# Solve following problem of dictionary 

# Input dictionary
a = {'a': 0, 'b': 1, 'c': 2}
b = {'az': 0, 'bz': 1, 'cz': 2}

# Output dictionary
{'az': {'a': 0}, 'bz': {'b': 1}, 'cz': {'c': 2}}


class Classifier:
    def __init__(self,d1,d2):
        self.a = d1
        self.b = d2

    def Convert(self):
        self.op = dict()

        for key,value in self.b.items():
            for key1,value1 in self.a.items():
                if value == value1:
                    self.op[key] = {key1 : value1}
        return self.op


def main():
    print("Application for Dictionary demonstration")
    a = {'a': 0, 'b': 1, 'c': 2}
    b = {'az': 0, 'bz': 1, 'cz': 2}

    obj = Classifier(a,b)
    ans = obj.Convert()
    print("Dictionary after demonstration : ",ans)

if __name__ == "__main__":
    main()