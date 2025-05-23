# Multiple inheritance : inherit from more than one parent class
#                        C(A,B)

# Multilevel inheritance : inherit from a parent which inherit from another parent
#                          C(B) <- B(A) <- A

# GrandParent class
class animal():
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

# Parent classes
class prey(animal):
    def flee(self):
        print(f"{self.name} is fleeing.")

class predator(animal):
    def hunt(self):
        print(f"{self.name} is hunting.")

# Child classes
class rabbit(prey):
    pass

class hawk(predator):
    pass

class fish(prey, predator):
    pass

rabbit = rabbit("Bugs")
hawk = hawk("Tony")
fish = fish("Nemo")

print("Fleeing is inherited from prey.")
rabbit.flee()
print("\n")

print("Hunting & Fleeing is inherited from predator.")
hawk.hunt()
print("\n")

print("Hunting is inherited from predator & prey.")
fish.flee()
fish.hunt()
print("\n")

print("Eating & Sleeping is inherited from animal.")
rabbit.eat()
hawk.sleep()
fish.eat()
