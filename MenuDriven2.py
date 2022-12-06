from MenuDriven1 import *

print('1. Addition\n'\
	'2. Subtraction\n'\
	'3. Multiplication\n'\
	'4. Division\n'\
	'5. Floor Division\n'\
	'6. Modules\n'\
	'7. Exponant\n'\
	'8. Exit')

# infinite while loop
while True :
	ch = int(input('Select your operation in integer :'))
	if ch == 1 :
		Add(int(input('Enter 1st number:')),int(input('Enter 2nd number:')))

	elif ch == 2 :
		Sub(int(input('Enter 1st number:')),int(input('Enter 2nd number:')))

	elif ch == 3 :
		Mul(int(input('Enter 1st number:')),int(input('Enter 2nd number:')))

	elif ch == 4 :
		Div(int(input('Enter 1st number:')),int(input('Enter 2nd number:')))

	elif ch == 5 :
		FDiv(int(input('Enter 1st number:')),int(input('Enter 2nd number:')))

	elif ch == 6 :
		Mod(int(input('Enter 1st number:')),int(input('Enter 2nd number:')))

	elif ch == 7 :
		Exp(int(input('Enter 1st number:')),int(input('Enter 2nd number:')))

	elif ch == 8 :
		print('Exit')
		break

	else :
		print('Invalid choice')

print('Program ends')