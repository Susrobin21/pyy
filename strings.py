#strings
a = 'wuefbwubkbwkab'
print(len(a))

#looping through strings

fruit='pineapple'
index = 0
while index < len(fruit):
    letter = fruit[index]
    index = index+1
    print(letter,index)

fruit = 'banana'
for letter in fruit :
    print(letter)

#letter is aliteral keyword in strings


#slicing of strings

j = 'oppenheimer goat'
print(j[0:5])
#python excludes the last letter
print(j[12:13])
print(j[11:14])
#even the spaces have an index value.
print(j[3:100])
# there is no traceback 

#string concantenation
a = 'moshi'
b = 'moshiii'
y = a+b
print(y)
# no space value by default 
#but space can be added like in the below command :
y = a+ ' ' +b
print(y)
#we can use the same variableee !!!!!!

#logics
#use 'in' function to check bool in string
fruit = 'pear'
print('p' in fruit)
print('z' in fruit)

#string conversion 
geek = 'Goood Morningg'
gok = geek.lower()
doc = geek.upper()
print(gok)
print(geek)
print(doc)
#print(dir(geek)) #all the things we can do to a string 

#findimg in strings 
fruit = 'gigantamax'
f = fruit.find('max')
print(f)
k = fruit.find('ze')
print(k) #unfound values are returned with a '-1'

#string replacement
fou = 'hola amigos lol'
g = fou.replace('lol', 'hehe')
print(g)

#stripping of whitespace
g = '   demn lol   '
print(g.lstrip())
print(g.rstrip())
print(g.strip())

#startswith and find 
fou = 'hola amigos'
print(fou.startswith('h'))
print(fou.startswith('H'))
print(fou.find('l'))