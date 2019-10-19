class Rectangle():
    def __init__(self,a,b):
        assert (a>0) and (b>0)
        self.a = a
        self.b = b
    def Square(self):
        return self.a *self.b
    def Perim(self):
        return 2*self.a + 2*self.b
    def __str__(self):
        return "<Rectangle object: {}, {}>".format(self.a, self.b)

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def LengthTo0(self):
        return (self.x *self.x + self.y*self.y)**(1./2)
    def LengthToPoint(self,point):
        return ((self.x - point.x)**2 + (self.y-point.y)**2)**(1./2)
    def __str__(self):
        return "<Point object: {}, {}>".format(self.x,self.y)

p1 = Point(1,1)
p2 = Point(2,2)
r1 = Rectangle(1,2)
print(p1.LengthTo0())
print(p2.LengthTo0())
print(p1.LengthToPoint(p2))
print(r1)
