#tuples and dicts
#useful in numercials 
#they're immutable 
#once u create a tuple it cant be altered
y = (2,3,4,5,6,3,5,3,4,32)
print(y)
print(max(y))
#y[2]=  4
#print(y) not possible

(x,y)=(4,'none')
print(y)

#tuple and dict
h = dict()
h['doe'] = 3
h['joe'] = 9
for (i,j) in h.items() :
    print(i,j)

# or we can use the below code 
tupes = h.items()
print(tupes)

#tuples are comparable 
print((1,2,3) > (4,5,6))

#sorting 
d = {'w': 10, 'e':4, 'o': 3}
print(d.items())
print(sorted(d.items())) 

#sorting by values instead of a key ( data structure)
d = {'w': 10, 'e':4, 'o': 3, 'u':45}
zu = list()
for c , k in d.items() :
    zu.append((k,c))
print(zu)
zu = sorted(zu, reverse=True) 
print(zu)

c = {'l':15 , 'g' : 8, 'f': 13, 'r': 17}
print(sorted([(v,k) for k,v in c.items()]))