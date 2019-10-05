l = input("enter some sentance: ")
print(l)
try:
    l1 = l[3:4]
except:
    print("short value")
l2= l[len(l)-2]
l3 = l[0:5]
l4 =l[0:len(l)-2]
l5 = l[0::2]
l6 = l[1::2]
l7 = l[::-1]
l8 = l[::-2]
l9 = l[(len(l)-2): :-2]
l10 = l[len(l)-2:0:-1]
l11 = len(l)
print(l1,l2,l3,l4,l5,l6, l7, l8, l9, l10, l11, sep=' ', end='\n' )


