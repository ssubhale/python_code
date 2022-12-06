#2. for loop
'''
_for loop allways finite its never infinite, for loop is for iterable and integer sequence
_ in for loop range function for integer sequence, range function is used to generate integer sequence only

# range(start, end, step)
_positive sequence 

_start is optional(default +0)
_end is mendatory(end +1)
_step is optional(default +1)
_condition is less than compulsary

syntax :
for variable/counter in range (start, end, step)
	. . . . . . . .
	. . . . . . . .
#Ex. print 1 to 10

for i in range (1, 11, 1) :  #start, end, step
	print(i)

for i in range (1, 11) :  #start, end
	print(i)

for i in range (21) :  #end
	print(i)

for i in range(1,11,1):
    print(i)

for i in range(10,0,-1):
    print(i)


#_negative sequence

_start is mandatory
_end is mendatory(end   - 1)
_step is mendatory (wth  -ve sign)
_condition is greater than

'''

#print 10 times Jay Shriram
for i in range(10, 0,  -1) :
	print("Jay Shriram")


# print 1 to 10
for i in range(1,11,1):
        print(i)


# print 10 to 1
for i in range(10,0,-1):
    print(i)
