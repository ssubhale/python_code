
##Nested list :-
#_list inside another list, acess elements by indexing


listM = [10,20,['abc',[8,5],3.2,1],30,40]
         #0   1           2          3  4
##_Indexing ex.

print('len of list is',len(listM))

print(listM[2][2])

print(listM[2][1][0])

print(listM[2][1][1])

print(listM[2][-1])

print(listM[2][0])

print(listM[-3][-1])

print(listM[3])

print(listM[-1])



##Ex.
mh = ['Pune','Mumbai']
gj = ['Surat','Bhuj']
india = [mh,gj]

print(india)

print(india[0][0])

print(india[0][1])

print(india[1][0])

print(india[1][1])


##for loop for nested list
for state in india:
    #print(state)
    for city in state:
       print(city)
