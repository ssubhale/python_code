##Dictionary

# Dictionary is used to store data in key:value pair, its mutable, insertion order is preserved from 3.7ver of python
# keys are immutable, value can be mutable as well as immutable, If we try to duplicate key then updated key considered
# Notation is {}, key value pair separated by colon : , indexing and slicing is not allowed


#syntax
'''
to creat empty dictionary
d = {}
or
d = dict()

to create dictionary with values
d = {1:'Python',2:'Java',3:'C++'}
'''


#Ex.
lang = {1:'Python',2:'Java',3:'C'}
print(lang)

##add values
lang[4] = '.Net'
lang[5] = 'JavaScript'
print(lang)

##duplicate keys
lang[2] = 'R'
print(lang)

lang[2] = 'Java'
print(lang)

##update values
lang[3] = 'C++'
print(lang)

##update dictionary
lang.update({6:'Asp.Net',7:'Ruby'})
print(lang)



###Dictionary methods

#EX.To access the elements in dictionary
lang = {1: 'Python', 2: 'R', 3: 'C++'}


for i in lang:
    print(i)  #it returns keys from dictionary

for j in lang.keys():
    print('.keys() : ',j)  #keys method return list of keys

for k in lang.values():
    print('.values() : ',k)  #values method returns list of values

for k,v in lang.items():
    print('.items() : ',k,v)  #items method returns list of tuples of keys and values

dic = {1:'Python', 2:'R', 3:'C++', 4:'.Net'}

dic2 = dic.copy()
print('dic=>',dic)
print('dic2=>',dic2)

dic.update({5:'Asp.Net', 6:'Ruby'})
print('dic.update()=>',dic)

dic.clear()
print('dic.clear()=>',dic)



k = [1,2,3,4]
v = ['a','b','c','d']
print(dict(zip(k,v)))