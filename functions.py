#function
def add(a,b):
    ado = a+b
    return ado
y = add(5,6)
print (y)
print(type(y))

#simple loop
for j in [1,2,3,4,5] :
    print(j)
print('done bitch !')

#string loop
foe = ['jo','ko','ho']
for foe in foe :
    print('kill : ',foe)
print('exterminated')

#largest num loop
largest = 0
print('before',largest)
for i in [3,67,45,87,132,64] :
    if i>largest :
        largest = i
    print('largest',i)
print('after',largest)

#count in loop
count = 0
for i in [2,43,56,65,123,45,67,1,2,3,8,7] :
    count = count +1
    print(count,i) #value and count
print(count) #only count

#adding in loops
sum = 0
for i in [2,43,56,65,123,45,67,1,2,3,8,7] :
    sum = sum +i
print(sum) 
#for average, use sum/count

#boolean search
found =False
for i in [16,7,64,32,44,4,9,12] :
    if i ==4 :
        found = True
    print(i,found)

# is can be used in place of ==, 'is' is stronger than ==
# 0 == 0.0 is true but 0 is 0.0 id false