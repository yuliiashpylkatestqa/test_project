a = int( input("a = "))
b= int(input("b = "))
c= int(input("c = "))

print(a,b,c)
if a==b==c:
    print("3")
else:
    if a==b or a==c or b==c:
        print("2")
    else:
        print("0")