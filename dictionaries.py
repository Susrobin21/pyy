#dictionaries

dot = dict()
dot['ryu'] = 23
dot['mofo'] = 89
dot['san']= 9
print(dot)
print(dot['mofo'])
dot['ryu'] = dot['ryu'] + 45
print(dot['ryu'])

chuck = {'olo' : 56,'opo': 69,'ono':34}
print(chuck)

#counting using dict
counts = dict()
name = ['meh', 'deh','ehh','neh','deh','meh','meh']
for i in name :
    if i not in counts :
        counts[i] = 1
    else :
        counts[i] = counts[i]+1
print(counts)
print(counts.get(i,0))

#simplified version of above code using get
counts = dict()
name = ['meh', 'deh','ehh','neh','deh','meh','meh']
for i in name :                                              #if i in counts : x = counts[i] 
    counts[i]= counts.get(i,0)+1                             #else : x = 0 
print(counts)  


#counting words

#listo = dict()
#line = input('')
#words = line.split()
#for word in words :
    #listo[word] = listo.get(word,0) +1
#print(listo)

#######
print(chuck.keys())
print(chuck.values())
print(chuck.items())