# Pattern printing
# Q. print the following number pattern using for loop
'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''

n = 5
for i in range(n):
    for j in range(i+1):
        print(i+1,end=" ")
    print()