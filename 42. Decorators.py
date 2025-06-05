# Decorator : A function that extendes the function of another function w/o modifing the base function
#             Pass the base function as the argument to the decorator
#             
#             @add_sprinkles
#             get_ice_cream("vanilla")

# Decorator
def add_sprinkles(func):
    def wrapper(*args,**kwags):
        print("You add sprinkles....")
        func(*args,**kwags)
    return wrapper 
def add_fudge(func):
    def wrapper(*args,**kwags):
        print("You add fudge....")
        func(*args,**kwags)
    return wrapper

@add_fudge
@add_sprinkles
# base function
def get_ice_cream(flavor):
    print(f"Get your {flavor} ICE CREAM....")

get_ice_cream("Vanilla")
get_ice_cream("Choclate")
