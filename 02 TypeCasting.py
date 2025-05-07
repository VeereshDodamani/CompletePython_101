## Type Casting: Process of converting a variable from one datatype to another datatype str(), int(), float(), boolean()

name = "Veeresh"
age = 25
gpa = 7.5
student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

# float -> int
gpa = int(gpa)
print(gpa)

# int -> float
age = float(age)
print(age)

# int -> str
age = str(age)
print(age)

# str -> boolean
name = bool(name)
print(name)
