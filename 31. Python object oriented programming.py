# Objests = A "bundel" of related attributes (variables) and methods (function)
#           Ex = phone, cup, book
#           You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object


class Car:
    # Constructive methods
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

car1 = Car("Mustang",2024,"Red",False)
print(car1)
print("\n")

car2 = Car("Corvette", 2025, "Blue", True)
# . (dot) is a Attribute access operator
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
print("\n")
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)
