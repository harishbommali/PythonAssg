from random import *
l=list()
for i in range(0,20):
    i=randint(0,30)
    l.append(i)
print(l)
s=set(l)
print('the length of list:',len(l))
print('the length of the set without duplicates:',len(s))
print('the no.of duplicates:',(len(l)-len(s)))
