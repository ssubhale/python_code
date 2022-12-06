## 6.Identity operators
'''
Identity operators are used to compare the memory location of two objects,
especially when both the objects have same name and can be differentiated
only using its memory location.
There are two Identity operators: "is" and "is not" .
'''

m = 12
n = 12

#is --> return true if both variables are the same object (same as == )
print(m is n, m == n)       #True True

#is not --> return true if both variables are not same object (same as != )
print(m is not n, m != n)   #False False
