##3 Set

#1.Set are use to store multiple objects with single name
#2.Set is mutable but It allows the store only immutable elements
#4.It does not allows duplicate elelments in it 
#5.Insertion order is not preserve, It does not support indexing and slicing 
#8.Set are mainly used to perform mathematical operartions such as union and intersection
#9.Notation is{}

##syntax

#to create empty set
#set_name = set() ##valid
#print(set_name)--> class 'set'
#set_name ={}  ##invalid
#print(set_name)--> class 'dictionary'

#to create set with values
#set_name = {1,3,7,'abc',True,False,4}


##Iteration
s = {10,20,30,40,50,60}
for i in s:
    print(i)


## Methods for set

s = {10,11,32,45,95,43,21,33,56}
#1 .add()   Add the element in set
s.add(48)
print('.add(48) -->>',s)

#2 .copy()  Create a copy of set
print(s)
s2 = s.copy()
print('.copy() -->>',s2)

#3 .discard(x)  It discard the element if is a member of set, Its return none when not found.
s.discard(45)
print(".discard() -->>",s)

#4 .pop()   It pop the first element in set, if set is empty KeyError is raised
s.pop()
print(".pop() -->>",s)

#5 .remove(x)    It remove the specified element, If not in set return KeyError
s.remove(21)
print(".remove() -->>",s)

#6 .update({x,y,z})    It update by set in existing set
s.update({1,2,3,4,5})
print(".update({1,2,3,4,5}) -->>",s)

