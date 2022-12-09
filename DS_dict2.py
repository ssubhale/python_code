
## Nested dictionary

d = {'emp1':
     {'name':'Ram','salery':25000,'dept':'IT','lang':{'lang1':'English','lang2':'German'}},
     'emp2':
     {'name':'Karan','salery':35000,'dept':'IT','lang':{'lang1':'English','lang2':'Spanish'}}

     }

##We access the values by using the keys
#Ex.
print(d['emp1']['lang'])

print(d['emp2']['dept'])

print(d['emp1'])

print(d['emp1']['lang']['lang2'])




##Ex.
mh = ['Pune','Mumbai']
gj = ['Surat','Bhuj']
s1 = ['c1','c2']
s2 = ['c3','c4']

india = {'Maharastra':mh,'Gujrat':gj}
usa = {'State1':s1,'State2':s2}

world = {'India':india,'USA':usa}
print(world)

for country,i in world.items():  #.item method
    print(country)
    for state, j in i.items():   #.item method
        print(state)
        for city in j:  #iteration
            print(city)




## Iterate a dictionary 
#Ex.

mh = ['Pune','Mumbai']
gj = ['Surat','Bhuj']
texas = ['Austin','Haustin']
washington = ['Olympia','Seattle']

india = {'Maharastra':mh,'Gujrat':gj}
usa = {'Texas':texas,'Washington':washington}

world= {'India':india,'USA':usa}
#print(world)

for country,i in world.items():
    print(country)
    for state,j in i.items():
        print(state)
        for city in j:
            print(city)