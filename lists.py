#list def
x = [1,2,3]
print(x)
y = [2,3,4,[9,0]]
print(y)
z = []
print(z)

#list using for loop 

for k in [1,2,3,4,5] :
    print(k)


#list length
op = ['george joestar'] 
print(len(op))


#printing elements in list
genshin = ['yelan', 'hu tao', 'raiden']
for character in genshin :
    print ('hello bbg', character)
print('hellowed all of them')

#printing position
gee = ['dog','cat','bird']
print(gee[1])

#how lists are mutable
ho = [2,55,44,3,5,2,55]
ho[2]= 42
print(ho)

#printing range, use len function 
print(range(len(ho)))

#using loops and range 
foe = ['mus','gus','cus','bus','zus']
for i in range(0,3):     # we can also use range(len(foe)) to print the whole list
    foes = foe[i]
    print('killed',foes)

#concatenating of lists 
a = [1,2,3,4,5,7]
b = [4,5,6,7]
c = a+b
print(c)

#slicing of lists
print(a[0:2])
print(a[:]) #full list printed

#making list from scratch 
k = list()
print(k)
k.append('howdy')
k.append(90)
print(k)
print(90 in k)
print(1 in b)

#max min
print(max(b))
print(sum(a))
print(min(b))
print(len(a))
print(sum(a)/len(a))

#simple sum calci
#lista = list()
#while True:
    #o = input('enter a number :')
    #if o =='done' : break
    #value = int(o)
    #lista.append(value)
#print(lista)
#average = sum(lista)/len(lista)
#print(average)

#split function
a = 'cocogoat is always sleepy af'
b = a.split()
print(b)
c = 'who;the;heck;are;you'
print(c.split())
print(c.split(';'))  # we can split based on paramters other than white spaces
