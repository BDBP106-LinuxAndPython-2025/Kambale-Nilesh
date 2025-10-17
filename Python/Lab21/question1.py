# #(1) Create a class called Quadrilateral that takes in four parameters - side1, side2, side3 and
# side4. Write two functions isSquare() and isRectangle() that checks for all the sides
# being equal (for a square) and the opposite sides being equal (for a rectangle), and returns
# True/False. Create an instance of the Quadrilateral with (a) all sides being different,
# (b) Opposite sides being same, (c) all sides being the same. Print the appropriate output.

class Quadrilateral():
    def __init__(self, w, x, y,z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    def issquare(w, x, y, z):
        return x==y and y==z and z==w

    def isrectangle(w,x,y,z):
        return w==y and x==z

    def deffsides(self):
        if self.x!=self.y and self.y!=self.z and self.z!=self.w:
            print('For given sides of quadrilateral are different ')
        else:
            print('For given sides of quadrilateral are not different ')
    def opposides(self):
        if self.x==self.y and self.x==self.z:
            print('For given quadrilateral opposite sides are same')
        else :
            print('For given quadrilateral opposite sides are different ')
    def allsidesame(self):
        if self.x == self.y and self.y == self.z and self.z == self.w:
            print('For given quadrilateral all side are same')
        else:
            print('For given quadrilateral all side are not same')

print(Quadrilateral.issquare(10,10,10,10))
print(Quadrilateral.isrectangle(10,10,10,20))



a = Quadrilateral(10,10,10,10)

a.deffsides()
a.opposides()
a.allsidesame()








