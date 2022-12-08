
## Common functions on list:

#1 len(list_name) = it give the total length of list.
#2 max(list_name) = it give maximum element of list.
#3 min(list_name) = it give minimum element of list.
#4 sum(list_name) = it give sum of all elements.

listx = [3,6,5,8,9,2,1,7]

print('Length of list : ',len(listx))

print('Maximum ele in list : ',max(listx))

print('Minimum ele in list : ',min(listx))

print('Sum of list : ',sum(listx))



#Mathematical operations on list

#_1.Addition + (joining two lists)
#_2.Multipliacation *  (multiply by non zero +ve integer only,repeatation of list)

listA = [1,2,3,4]
listB = [5,6,7,8]

print(listA + listB)

print(listB + listA)

print(listA * 2)

print(listB * 2)

print(listA * 0)

print(listA *  -2)

print(listA * 3.4)  #Error
