## 5.Membership operators-
'''
Membership operators which used to validate the membership of a
value.It test for membership in a sequence, such as strings, lists, or tuples.
'''

a = 'Fall in love with python programming'
l = [1,2,3,4,5,6,7]

#in --> return true if a sequence with the specified value is present in the object
print('f' in a)     #False
print('F' in a)     #True
print(5 in l)       #True

#not in --> return true if a sequence with the specified value is not present in the object
print('f' not in a)     #True
print('F' not in a)     #False
print(5 not in l)       #False
print(10 not in l)      #True