
# Scenario 4

x = 10 #global variable

def m1( ):
	a = 20 #local variable
	print('m1 : ', a)
	print('m1 : ', x)
def m2( ):
	a = 30 #local variable
	print('m2 : ', a) #Error
	print('m2 : ', x)
print(x)
m1( )
m2( )
