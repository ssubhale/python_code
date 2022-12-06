## Variales scope scenarios

#Local variable :
'''
_Local variable belongs to its scope is within a fuction or block.
_it is created when a block starts and destroyed when block ends.
_priority is given to local over global.
_it cann't be accessed outside the block or function.
_if we want to access it outside the block then we have return it from the function.
'''

#Global variable :
'''
_Global variable belongs to whole program.
_it is created when a program starts and destroyed when program ends.
_it can be access in whole program.
_if we want to update a global variable inside a block then use either global keyword
    or globals function. it gets update for whole program.
'''


# Scenario 1

x = 10 #global variable

def m1():
	print('m1 : ',x)
def m2():
	print('m2 : ',x)
print(x)
m1()
m2()
