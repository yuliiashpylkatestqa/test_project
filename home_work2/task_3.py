year = int(input("Year: "))

if ((year%4)!=0):
    print("No")
else:
    if (year%100==0) and (year%400!=0):
        print("No")
    else:
        print("Yes")