a = int( input("a = "))
b= int(input("b = "))
c= int(input("c = "))

print(a,b,c)
if (((a+b)>c) and ((a+c)>b) and ((b+c)>a)):
    print("yes")
else:
    print("no")