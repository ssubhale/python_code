# By the built-in input function we get any from user in our program
x = input("Enter your value : ")
print(x)
print(type(x))

# by default input function get user value in string datatype 
# If we want integer, float or boolean value we have to typecast it in other datatype

# if we want integer value
x = int(input("Enter integer value : "))
print(x)
print(type(x))

# if we want float value
y = float(input("Enter float value : "))
print(y)
print(type(y))

# if we want boolean value
z = bool(input("Enter boolean value : "))
print(z)
print(type(z))