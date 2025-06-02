# Magic methods : Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of python build in operations.
#                 They allow developers to define or customize the behaviour of object

class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f"name : {self.name}, gpa : {self.gpa}"
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __gt__(self, other):
        return self.gpa < other.gpa
        
student1 = Student("Harry",7.9)
student2 = Student("Jack",8.8)

print(Student)
print("Student1 gpa equal to Student 2: ",student1 == student2)
print("Student 1 gpa less than Student 2: ",student1 > student2)
