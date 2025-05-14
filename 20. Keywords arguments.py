## Keywords argument = an argument preceded by an indentifier
#                      helps with readability
#                      order of argument dosen't matter
#                      1. Positional, 2. default, 3. keywords, 4. arbitrary

def hello(greeting, title, first, last):
    print(f"My {greeting} {title}{first} {last}")

hello("Hello", "Mr.","Vee", "Dham")

# what if I want to change the sequence
hello(greeting="Hello",first="Vee", last="Dham", title="Mr.")
hello("Hello",first="Vee", last="Dham", title="Mr.")
