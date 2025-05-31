# Polymorphism : Greek words that means to have many forms or faces.
#                Poly = Many
#                Morphene = Forms

# Two ways to achieve polymorhism
#           1. Inheritance = An object could be treated of same type as a parent class
#           2. "Duck Typing" = Object must have necessary attributes/methods

class Shape:
    pass

class Circle(Shape):
    pass

class Square(Shape):
    pass

class Triangle(Shape):
    pass


# square is Square, square is Shape, but not circle, triangle
# square have two forms : Square and Shape
square = Square()
