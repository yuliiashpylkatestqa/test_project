import  math
from inputnum import inputnumber
def distance (x1, y1, x2, y2):
    d=math.sqrt(((x2-x1)**2)-((y2-y1)**2))
    return d

a=inputnumber()
b=inputnumber()
c=inputnumber()
d=inputnumber()
r=distance(a,b,c,d)
print(r)