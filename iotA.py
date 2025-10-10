#Area of circle using oops
import math
class circle:#inistalize the circle object with a given radius
    def __init__(self,r):
      self.r = r

    def calarea(self):
        return math.pi*self.r**2
    def cirper(self):
        return 2*math.pi*self.r

#driver code
r= float(input("input the radius of the circle:"))

a= circle(r)

area= a.calarea()

print("Area of the circle:",area)


  
