## default arguments = A default value for a certain parameter
#                      Default is used when that vallue is omitted

def net_price(list_price, discount, tax):
    return list_price * (1-discount) * (1+tax)

print(net_price(500, 0,  0.05))

# Let's consider that most of the times the discount is 0 and tax is 0.05
def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1-discount) * (1+tax)
print(net_price(500))

# if we pass the value then that will be considered rather than the default value
def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1-discount) * (1+tax)
print(net_price(500, 0.1, 0))
