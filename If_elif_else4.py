## Write a python program, to take value from user 1 to 7 and assign 1 to 7 by Monday to Sunday. If no is not in 1 to 7 then ask for valid input.

num  = int(input("Please your number for display weekdays : "))

if num == 1:
	print("Monday")

elif num == 2:
	print("Tuesday")

elif num == 3:
	print("Wednesday")

elif num == 4:
	print("Thursday")

elif num == 5:
	print("Friday")

elif num == 6:
	print("Saturday")

elif num == 7:
	print("Sunday")

else:
	print("Please enter num. between 1 to 7")
