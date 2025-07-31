#Create a text file how many words line character it contain.If do not known file handling, then take input from user intructed
line=input('enter string:')
l=0
line2=line.split('.')
for i in line2:
    l+=1
print(l)

#count words
w=0
word=line.split()
for i in word:
    w+=1
print("Total word are ",w)

#count character
c=0
for i in word:
    for j in i:
        c+=1
print("Total character are",c)

