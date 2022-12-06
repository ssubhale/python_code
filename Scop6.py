
# Scenario 6

#Update the global variable by using global function
x = 10 #global variable

def m1( ):
	#globals()['x'] = globals()['x'] + 10
	globals()['x'] += 10
	print('m1 : ', x)
def m2( ):
	print('m2 : ', x)
print(x)
m1( )
m2( )
