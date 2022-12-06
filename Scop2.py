# Scenario 2

x = 10  #global variable

def m1():
	x = 20 #local variable
	print('m1 : ',x)
def m2():
	print('m2 : ',x)
print(x)
m1()
m2()
