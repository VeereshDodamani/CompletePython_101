# "DUCK TYPING" : this is a another method to achieve polymorphism beside inheritance
#                 Objects must have the minimum necessary attributes/methods.
#                 "If it looks lia a duck and quacks like a duck, then it must be a duck"

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("Meoww")

# Our car dpsen't have minimum necessary attributes/methods
# Speak and alive
# class Car():
#     def horn(self):
#         print("HONK!")

class Car():
    alive = False
    def speak(self):
        print("HONK!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)
