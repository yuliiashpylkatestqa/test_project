from inputnum import inputnumber
def triangle (a,b,c):
    if (a==b) or (a==c) :
        return("Isosceles triangle")
    elif ((a==b) and (a==c) and (b==c)):
        return ("Equilateral triangle ")
    elif a!=b!=c:
        return ("Versatile triangle ")
    else:
        return ("Not a triangle")
a=inputnumber()
b=inputnumber()
c=inputnumber()
r=triangle(a,b,c)
print(r)