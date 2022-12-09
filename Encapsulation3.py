## Inheritance in encapsulation

class A:
    a = 15
    _b = 25
    __c = 35

    def m1(self):
        print('Public method')

    def _m2(self):
        print('Protected method')
        print(self.__c)

    def __m3(self):
        print('private method')

class B(A):
    def m1(self):
        print(self.a)
        print(self._b)
        #print(self.__c) # AttributeError: 'B' object has no attribute '_B__c'
        super().m1()
        super()._m2()
        #super().__m3() # AttributeError: 'super' object has no attribute '_B__m3'

def main():
    print("Inheritance in encapsulation")
    print(b._A__c)
    b = B()
    b.m1()
    b._A__m3()

if __name__ == "__main__":
    main()