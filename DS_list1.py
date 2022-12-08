##1_List

#_list is used to hold multiple elements into a single variable.

#Propertise of list
'''
1.List is mutable(it can be changed)
2.It allows heterogeneous elements( elements of diffrent data types)
3.Insertion order is preserved( it maintain the sequence start to ends)
4.Duplicates are allowed
5.Indexing and slicing are allowed
6.Notation is [ ]
'''
# syntax:
'''
to create empty list
list_name = [ ]

to create list
list_name = list()  #list function is return the object function

to create list with values
a = [e1,e2,e3,e4,e5]
'''


##Methodes in list

listN = [5,10,25,15,10]
print('Original list is:',listN)

#1 .append(...) ---> it add the single element at the end
listN.append(35)
print('.append(35):',listN)

#2 .extend([...]) ---> it add the multiple element at end
listN.extend([40,45,50])
print('.extend([40,45,50]):',listN)

#3 .insert(index,element) ---> add elelments at specified index
listN.insert(3,20)
print('.insert(3,20):',listN)

#4 .pop() ---> removes the last element
listN.pop()
print('.pop():',listN)

# .pop(i) = removes elelment for specified index
#listN.pop(12)   #IndexError: pop index out of range
listN.pop(5)
print('.pop(5):',listN)

#5 .remove(x) = removes specified element
#listN.remove(13)    #ValueError: list.remove(x): x not in list
listN.remove(10)
print('.remove(11):',listN)

#6 .sort() = it sort the list in ascending order
listN.sort()
print('.sort():',listN)

# .sort(reverse=True) = it sort the list in descending order
listN.sort(reverse = True)
print('.sort(reverse=True):',listN)

#7 .reverse() = reverse the list
listN.reverse()
print('.reverse():',listN)

#8 .index(x) = return the index of the first match element
#a = listN.index(0)  ##ValueError: 0 is not in list
a = listN.index(20)
print('.index(20):',a)

#9 .count(x) = return the count of element which is passed as an argument
x = listN.count(15)
print('.count(15):',x)

#10 .copy() = return a copy of the list
listO = listN.copy()
print('.copy():',listO)

#11 .clear() = its clear all the items in the list
listN.clear()
print('.clear():',listN)
