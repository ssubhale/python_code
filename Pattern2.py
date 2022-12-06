# Pattern printing

# Q. print following pattern using while and for loop
'''
* 
* * 
* * * 
* * * * 
* * * * *
'''

i = 1
while i <= 5:
    print("* " * i)
    i += 1

print("---------------------------------------------------------------")

for i in range(1,6,1):
    print("* " * i)