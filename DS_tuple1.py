
##2_Tuple

# Tuples are used to store multiple items in a single variable. Tuple are immutable(once we define its not change)
#_It allows heterogenous elements and Duplicates also. Insertion order is preserved, Indexing and slicing are allowed
#_notation is ( )


#syntax
#to create empty tuple
#tuple_name = ()
#tuple_name = tuple()

##to create tuple with values
#tuple_name = (2,4,3,'pqr',True,False,8)
#tuple_name = 2,4,3,'pqr',True,False,8

##to add single element in tuple
#tuple_name = (1,)  or  (6.4,)

#_if we try to update tuple it will gives type error as tuple is immutable

## Iteration
#_iterating a tuple by using for loop
t = (1,2,3,4,5,6,7)
for i in t:
    print(i)
 
## Nested tuple
    
mh = ('Pune','Mumbai')
gj = ('Surat','Bhuj')
india = (mh,gj)

print(india)

##for loop for nested tuple
for state in india:
    for city in state:
        print(city)


