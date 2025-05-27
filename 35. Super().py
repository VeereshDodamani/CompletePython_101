## super() : Function used in a child class to call methods from a parent class (superclass).
#            Allow to you extend the functionality of the inherited class.

class Circle:
    def __init__(self, color, filled, radius):
        self.color = color
        self.filled = filled
        self.radius = radius

class Square:
    def __init__(self, color, filled, width):
        self.color = color
        self.filled = filled
        self.width = width

class Triangle:
    def __init__(self, color, filled, width, height):
        self.color = color
        self.filled = filled
        self.width = width
        self.height = height

# Now suppose if you change the variable name of filled with is_filled then you need to change it everywhere manually.
# That's where super() or inheritance can come in function

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

circle = Circle(color="Red",is_filled=True, radius=5)
print("Circle info: ")
print("Circle color: ",circle.color)
print("IS filled: ",circle.is_filled)
print("Radius of circle: ",circle.radius)
circle.describe()
print("\n")

triangle = Triangle(color="Blue",is_filled=False, width=10, height=12)
print("Triangle info: ")
print("Triangle color: ",triangle.color)
print("IS filled: ",triangle.is_filled)
print("Width of Triangle: ", triangle.width)
print("Height of Triangle: ",triangle.height)
triangle.describe()
print("\n")

square = Square(color="Green",is_filled=True, width=5)
print("square info: ")
print("square color: ",square.color)
print("IS filled: ",square.is_filled)
print("Width of square: ", square.width)
square.describe()
