# All arithmatic operations in one function


def add(no1, no2) :
	print('Addition : ',no1 + no2)
def sub(no1, no2) :
	print('Subtraction : ',no1  - no2)
def mul(no1, no2) :
	print('Multiplication : ',no1 * no2)
def div(no1, no2) :
	print('Division : ',no1 / no2)
def floordiv(no1, no2) :
	print('Floor division : ',no1 // no2)
def mod(no1, no2) :
	print('Modulous : ',no1 % no2)
def exp(no1, no2) :
	print('Exponant : ',no1 ** no2)

def main():
	a = 15
	b = 4
	add(a, b)
	sub(a, b)
	mul(a, b)
	div(a, b)
	floordiv(a, b)
	mod(a, b)
	exp(a, b)
if __name__ == "__main__":
	main()