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

# setter method
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be > 0")
            print("\n")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be > 0")
            print("\n")

# deleter method
    @width.deleter
    def width(self):
        del self._width
        print("Width have been deleted")
    
    @height.deleter
    def height(self):
        del self._height
        print("Height have been deleted")


rectange = Rectangle(3,4)

rectange.width = 0
rectange.height = 5

print("Getting the direct private variable")
print(f"Width : {rectange._width}, Height : {rectange._height}")
print("Using the getter method")
print(f"Width : {rectange.width}, Height : {rectange.height}")
print("\n")

del rectange.width
del rectange.height
