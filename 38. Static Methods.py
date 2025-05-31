# Static Methods : A emthod that belong to a class rather than a object from the class (instance)
#                  Used uaually for general utility function

# Instance method : Best for operations on instances of the class
# Static method : Best for utility functions that do not need access to class data

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    # we don't need to relay on any object to use this method
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook"]
        return position in valid_positions

# For a static method, you only need to access the class, no need to create any object for that class
# No need of this
# employee1 = Employe()
print(Employee.is_valid_position("Security"))
print(Employee.is_valid_position("Cook"))

# For a instance method, you access an object then call the instance method 
employee1 = Employee("Harry","Manager")
print(employee1.get_info())
employee2 = Employee("Jack","Cashier")
print(employee2.get_info())
