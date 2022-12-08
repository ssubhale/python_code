
##Mathematical operations on tuple

#_1 + (joining two tuple)
#_2 * (multiply by non zero +ve integer,repeatation of tuple)

t1 = (1,2,3)
t2 = (4,5,6)

print(t1 + t2)

print(t2 + t1)

print(t1 * 2)

print(t2 * 2)

print(t1 * 0)




## Methods in tuple
#1.count(x) = it count the occurence of the given element
#2.index(i) = it returns the index of first occurence of given element

x = (3,2,7,9,2,4,2,6)

print(x.count(2))

print(x.index(9))