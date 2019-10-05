from inputnum import inputnumber
def triangle (a,b,c):
    if (((a+b)>c) and ((a+c)>b) and ((b+c)>a)):
        return("yes")
    else:
        return ("no")
a=inputnumber()
b=inputnumber()
c=inputnumber()
r=triangle(a,b,c)
print(r)