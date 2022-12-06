
#1. while loop
	#finite while loop
	#infinite while loop
'''
The while loop in Python is used to iterate over a block of code as long as the test condition is true.
A finite while loop ends itself. An infinite while loop will not end without an outside cause.

#infinite while loop
syntax : 
while True:
	. . . . . . . . . .
	. . . . . . . . . . 

#finite while loop
syntax :
initialision of variable or counter
while condition/end :
	. . . . . . . . . . . 
	. . . . . . . . . . .
	increment decrement of counter
'''

# Ex. finite while loop
# print 10 times Jay Shriram

i = 1
while i <= 10:
    print("Jay Shriram")
    i += 1


# print 1 to 10 using while loop
i = 1
while i <= 10:
    print(i)
    i += 1

# print 10 to 1 using while loop

i = 10
while i >= 1:
    print(i)
    i -= 1

