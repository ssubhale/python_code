
# Scenario 3

x = 10 #global variable

def m1(x):# x = 25 local variable
	print('m1 : ',x)

def m2():
	print('m2 : ',x)
print(x)
m1(25)
m2()
