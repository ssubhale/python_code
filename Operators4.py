## 4.Logical operators
'''
Logical operators perform boolean operations on data and return a boolean result
(true or false), depending upon the statement's conditions.
'''

x = 12
y = 20

#and --> returns true if both conditions are true, otherwise false
print(x == 12 and x < y)                #True
print(x == 12 and x < y and x == y)     #False

#or --> returns true if one of the condition is true, otherwise both condition false then it return false
print(x == 12 or x < y)                 #True
print(x == 12 or x == y or x > y)       #True
print(x > y or x == y)                  #False

#not --> reverse the result, return true if condition is false and return false if condition is true
print(not x != y)       #False
print(not x > y)        #True

