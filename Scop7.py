
# Scenario 7

#Update the global variable by using global function
x = 10 #global variable

def m1( ):
	x = 20
	print('local x : ', x)
	print('global x : ', globals()['x'])
	x = x + 10
	print('update local x : ', x)
	globals()['x'] = globals()['x'] + 10
	print('update global x : ', globals()['x'])
def m2( ):
	print('m2 : ', x)
print(x)
m1( )
m2( )
