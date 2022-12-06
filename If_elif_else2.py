#2. if else statement
'''
syntax :
if condition :
	. . . . . . . . . .
	. . . . . . . . . .
else :
	. . . . . . . . . .
	. . . . . . . . . .

Rulls :
condition become True control goes inside if block
condition become False control goes inside else block
'''

print('Hello')
age = int(input('Enter age : '))

if age >= 18 :
	print('Eligible for vote')

else :
	print('Not eligible for vote')

print('Bye !')
