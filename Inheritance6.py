#5 Hybrid inheritance(combination of multiple & hierarchical)
## Diamond problem
class PMC:
    def __init__(self,name,location):
        self.name = name
        self.location = location
    def __str__(self):
        return f'Municipal corportion name:{self.name}\nLocation:{self.location}'
class Transport(PMC):
    def __init__(self,start,end):
        self.start = start
        self.end = end
        print('Health details')
        super().__init__(input('Enter dieseas:'),input('Enter hospital name:'))
    def __str__(self):
        print(super().__str__())
        return f'Start point:{self.start}\nDestination point:{self.end}'

class Health(PMC):
    def __init__(self,dieseas,hospital):
        self.dieseas = dieseas
        self.hospital = hospital
        super().__init__(input('Enter muncipal corporation name:'),input('Enter location:'))
    def __str__(self):
        print(super().__str__())
        return f'Dieseas:{self.dieseas}\nHospital:{self.hospital}'
    
class Voter(Transport,Health):
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
        print('Traveling details')
        super().__init__(input('Pick up point:'),input('End point:'))       
    def __str__(self):
        print(super().__str__())
        return f'Your name:{self.name}\nAge:{self.age}, Address:{self.address}'
    
n = int(input('Enter a no of voter:'))
for i in range(n):
    v = Voter(input('Enter name:'),int(input('Enter age:')),input('Enter address:'))
    print(v)

