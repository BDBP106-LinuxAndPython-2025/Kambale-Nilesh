# (2) Idea of inheritance- parent and child classes. Extend the Quadrilateral class with two
# child classes - Square and Rectangle. In the constructor of the child classes, call the
# parent’s constructor with a single side or 2 sides as the case may be. Define functions
# getArea() in the child classes that return the area of the square or the rectangle.

class Quadrilateral():
    def __init__(self, w, x, y, z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z

class Square(Quadrilateral):
    def __init__(self,side):
        super().__init__(side,side,side,side)

    def getArea(self):
            return self.w*self.x


class Rectangle(Quadrilateral):
    def __init__(self,length,breath):
       super().__init__(length,breath,length,breath)

    def getArea(self):
            return self.w*self.z



a = Quadrilateral(3,9,8,9)
b = Rectangle(2,3)
print(b.getArea())
c = Square(5)
print(c.getArea())










