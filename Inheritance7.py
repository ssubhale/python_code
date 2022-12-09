class A:
    x = 10
    y = 20

    def m1(self):
        print("m1---A")

    def m2(self):
        print("m2---A")
a = A()
print(a.x)          # 10
print(a.y)          # 20
a.m1()              # m1---A
a.m2()              # m2---A

## **************************************************************

class B:
    x = 50
    z = 100

    def m2(self):
        print("m2---B")

    def m3(self):
        print("m3---B")
b = B()
print(b.x)          # 50
print(b.z)          # 100
b.m2()              # m2---B
b.m3()              # m3---B

## ***************************************************************

class C(A,B):
    y = 200
    p = 300

    def m2(self):
        print("m2---C")

    def m4(self):
        print("m4---C")

    def m5(self):
        print("m5---C")
c = C()
print(c.x)          # 10

print(c.y)          # 200
print(c.p)          # 300
print(c.x)          # 10
c.m1()              # m1---A
c.m2()              # m2---C
c.m3()              # m3---B
c.m4()              # m4---C
c.m5()              # m5---C

## ***********************************************************************

class D(C):
    p = 800
    y = 900

    def m4(self):
        print("m4---D")

    def m6(self):
        print("m6---D")
d = D()
print(d.x)      # 10
print(d.y)      # 900
print(d.z)      # 100
print(d.p)      # 800
d.m1()          # m1---A
d.m2()          # m2---C
d.m3()          # m3---B
d.m4()          # m4---D
d.m5()          # m5---C
d.m6()          # m6---D

## ***********************************************************************

class E(C):
    w = 600
    q = 700
    p = 300

    def m4(self):
        print("m4---E")

    def m7(self):
        print("m7---E")
e = E()
print(e.w)      # 600
print(e.q)      # 700
print(e.p)      # 300
print(e.x)      # 10
print(e.y)      # 200
print(e.z)      # 100
e.m1()          # m1---A
e.m2()          # m2---C
e.m3()          # m3---B
e.m4()          # m4---E
e.m5()          # m5---C
e.m7()          # m7---E








