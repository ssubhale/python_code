# Pattern printing
# Q. print following pattern using while and for loop
'''
* * * * *
  * * * *
    * * *
      * *
        *
'''
i = 5
while i >= 1:
    print("  " * (5 - i) + " *" * i)
    i -= 1

print("-----------------------------------------------")

for i in range(5,0,-1):
    print("  " * (5-i) + " *" * i)