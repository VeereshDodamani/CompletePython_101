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
