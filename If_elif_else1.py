#1.Simple if statement 
'''
syntax : 
if condition :
	. . . . . . . . . .
	. . . . . . . . . .

Rulls :
in if statement:
condition is True control goes inside if block
condition is False control goes come out of if block
'''

print('Hello')
age = int(input('Enter age :'))
if age >= 18:
	print('Eligible to vote')
if age < 18:
	print('Not eligible to vote')
print('Bye !')
