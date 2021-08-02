a=input('Enter your string:').strip()
print('no of characters present in the string with out spaces:',len(a))
b=input('Enter your search letter:')
if b in a:
    print('no.of letters present in string:',a.count(b))
    c=a.find(b) #first occurence
    print('first occurence in string:',c)
    d=a.find(b,a.find(b)+1) #second occurence
    print('second occurence in stringu:',d)
else:
    print("the letter does't exist in string")
