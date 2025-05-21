# Inheritance : Allow the class to inherit attributes and methods from another class
#               Help with code reusability and extensibility
#               class Child(Parent)

class Animal():
    def __init__(self,name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")
    

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Mouse(Animal):
    pass

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Jerry")

# These are getting from class Animal
print("These are getting from class Animal")
print(f"Dog name : {dog.name}")
print(f"Dog is alive : {dog.is_alive}")
dog.eat()
dog.sleep()
print("\n")
print(f"Cat name : {cat.name}")
print(f"Cat is alive : {cat.is_alive}")
cat.eat()
cat.sleep()
print("\n")
print(f"Mouse name : {mouse.name}")
print(f"Mouse is alive : {mouse.is_alive}")
mouse.eat()
mouse.sleep()
