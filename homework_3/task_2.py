l=str(input("enter sentance: "))
l1 =str (l[0:int(len(l)/2)])
if len(l)%2==0:
    l2=str((l[int((len(l)/2)):])+ l1)
    print(l2)
elif len(l)%2!=0:
    l3 = str(l[0:int((len(l) / 2)+1)])
    l4 = str((l[int((len(l) / 2)+1):]) + l3)
    print(l4)