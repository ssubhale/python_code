
# Scenario 5

#Update the global variable by using global keywords
x = 10 #global variable

def m1( ):
	#x = x + 10  #Error
	global x
	x = x + 10 
	print('m1 : ', x)
def m2( ):
	print('m2 : ', x)
print (x)
m1( )
m2( )
