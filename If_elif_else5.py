
## Calculate electricity bill.
'''
	Unit				Price
	0 to 100			Free
	101 to 200			5 rs
	201 above 			10 rs
'''
unit = int(input("Enter your electricity unit : "))

if (unit <= 0):
	print("Please enter proper electricity unit")

elif (unit > 0 and unit <= 100):
	print("No electricity charge free of cost")

elif (unit > 100 and unit <= 200):
	res = (unit - 100) * 5
	print(f"Your electricity bill is : {res}rs")
	
else:
	res = (unit - 100) * 10
	print(f"Your electricity bill is : {res}rs")