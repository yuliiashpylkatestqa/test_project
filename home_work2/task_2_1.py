year = int(input ("Please enter year: "))

if year%4==0 or year%400==0 and year%100!=0:
    print("Yes")
else:
    print("No")



