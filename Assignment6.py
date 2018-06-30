#ques1:10 inputs from user and prnt it on screen
'''
print("Enter your 10 numbers")
p=[]
for i in range(10):
    a=input("Enter your number")
    p.append(a)
print("The"+str(i+1)+" number you entered"+str(p))

#ques2:infinite loop

l=[1]
for i in range(l):
    l.append(i)
    print(i)


#ques 3:integer list...and square its elements
a=[]
for i in range(5):
    b=input("Enter your elements")
    a.append(b)
sq=[]

sq=[int(i)**2 for i in a]

print(sq)

#ques 4:lists of type ints,string and floats and add them to seprate list
from random import shuffle
l=[]
ints1=[]
st1=[]
flo1=[]
for i in range(2):
    ini=int(input("Enter integers values"))

    strr=str(input("Enter string values"))

    fll=float(input("Enter float values"))
    l.append(ini)
    l.append(strr)
    l.append(fll)
shuffle(l)

for i in l:
    if type(i) is int:
        ints1.append(i)
    elif type(i) is float:
        flo1.append(i)
    else:
        st1.append(i)

print("ints"+str(ints1)+"floats"+str(flo1)+"string"+str(st1))

#ques 5:even and odd of range(1,101) into difffrent lists
even=[]
odd=[]
for i in range(1,101):
    if not i% 2:
        even.append(i)
    else:
        odd.append(i)

print("even"+str(even)+"\n odd"+str(odd))

#ques 6:pattern

for i in range(0,4):
    print("")
    for j in range(0,i+1):
            print("* ",end="")

#ques 7:

dict = {'aa':1, 'bb':2, 'cc': 3, 'dd': 4}
for i in dict.values():
    for j in dict.keys():
        if i == dict[j]:
            print("\n found", i, "at key", j)
'''
#ques 8:
a=[]
for i in range(3):
    b=input("enter 3 numbers")
    a.append(b)

search = input("Enter a number to search")

for i in a:
    if i == search:
        a.pop(i)
        print("Element found and deleted")
    else:
        print("element not found")


