# syntax | list_name = {key :expression for (key,value) in iterable}

cart = {'phone':25000.00,'lamp':2560.60,'table':5499.61,'pen':20.50,'bag':650.20,'kettle':1500.00}

# target to store round off values in another dict
cart_rounded = {k:round(v) for (k,v) in cart.items()}
print(f"The output is {cart_rounded}")

cart_rounded = {k[0]:round(v) for (k,v) in cart.items()}
print(f"The output is {cart_rounded}")

cart2 = {k:v for (k,v) in cart.items() if v > 1000}
print(f"The output is {cart2}")

cart3 = {k:v*0.9 if v>20000 else v for (k,v) in cart.items()}       # 10% discount
print(f"The output is {cart3}")

