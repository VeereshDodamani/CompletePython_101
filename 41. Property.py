# @property  = Decorator used to define a method as property
#              It can be accessed like a attibute
#              Benifit : Add additional logic when read, write or delete attributes
#              Gives you getter, setter and deletor method


class Rectangle:
    def __init__(self, width, height):
        self._width = width # Private width
        self._height = height # Private height
# getter method
    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"


rectange = Rectangle(3,4)
print("Getting the direct private variable")
print(f"Width : {rectange._width}, Height : {rectange._height}")
print("Using the getter method")
print(f"Width : {rectange.width}, Height : {rectange.height}")
