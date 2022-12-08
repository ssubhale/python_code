
##Slicing :-
#_It is used to generate a sequence from a predefined sequence.
#  [::] slice operator
#_ positive slicing[::] left to right

# [start:end:step]
# [start:end]
# satrt is optional [default = 0]
# end is optional [default = -1]
# step is also optional [default = + 1]
# condition is less than



#Ex.
list = [10, 20, 30, 40, 50, 60]
        #0   1   2   3   4   5
       #-6  -5  -4  -3  -2  -1

print(list[0:3:1])

print(list[0:6:1])

print(list[ : : ])

print(list[ : ])

print(list[0:-1:])####

print(list[ : :2])

print(list[-4: : ])

print(list[-5:5:1])

print(list[-1:1:1])


#_negative slicing

#_start is optional(default -1)
#_end is optional (default o)
#_step is mendatory with -ve sign
#_condition is greater than

        #-5  -4  -3  -2  -1
listq = [10, 20, 30, 40, 50]
        # 0   1   2   3   4

print(listq[4:1:-1])

print(listq[-4:-1:-1]) ### [ ]

print(listq[ : :-1])

print(listq[ : :-2])

print(listq[-1:-2:-1])

print(listq[2: :-1])

print(listq[ :-4:-1])

print(listq[-3:3:-2])

print(listq[2:1:-2])



