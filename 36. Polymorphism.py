# Polymorphism : Greek words that means to have many forms or faces.
#                Poly = Many
#                Morphene = Forms

# Two ways to achieve polymorhism
#           1. Inheritance = An object could be treated of same type as a parent class
#           2. "Duck Typing" = Object must have necessary attributes/methods

from abc import ABC, abstractclassmethod
class Shape:
    @abstractclassmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius**2

class Square(Shape):
    def __init__(self,width):
        self.width = width
    
    def area(self):
        return self.width**2

class Triangle(Shape):
    def __init__(self,height,base):
        self.height = height
        self.base = base
    
    def area(self):
        return 0.5*self.base*self.height


# square is Square, square is Shape, but not circle, triangle
# square have two forms : Square and Shape
# square = Square()

shapes = [Circle(4), Square(5), Triangle(4,5)]

for shape in shapes:
    print(f"The area of {shape.area()} cm²")
