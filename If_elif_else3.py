#3. elif statement (shortform of else if = elif)
'''
syntax :
if condition :
	. . . . . . . . . .
	. . . . . . . . . .
elif condition :
	. . . . . . . . . .
	. . . . . . . . . .
elif condition :
	. . . . . . . . . .
	. . . . . . . . . .
else :
	. . . . . . . . . .
	. . . . . . . . . .

Rulls :
elif is use when there are multiple conditions in our program on same thing
where ever the condition is True only that block is executed and control comes
totaly outside when all conditions are False then else block is executed.
'''

marks = int(input('Enter your marks :'))

if marks >= 91 and marks <= 100 :
	print('A+')

elif marks >= 81 and marks <= 90:
	print('A')

elif marks >= 71 and marks <= 80:
	print('B+')

elif marks >= 61 and marks <= 70:
	print('B')

elif marks >= 51 and marks <= 60:
	print('C+')

elif marks >= 41 and marks <= 50:
	print('C')
	
elif marks > 100:
        print('Wrong input')

else :
	print('Fail')	
