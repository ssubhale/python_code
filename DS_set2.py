
##Nested set
#  set inside set

mh = {'Pune','Mumbai'}
gj = {'Surat','Bhuj'}

fmh = frozenset(mh)
fgj = frozenset(gj)

india = {fmh,fgj}

for state in india:
    for city in state:
        print(city)