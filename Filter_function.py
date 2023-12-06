
# filter(function,iterable) | to filter
items = [(3456,"Shoe",780),(3556,"Phone",21000),(2587,"Book",450),(5412,"Pen",75)]
less_than_500 = lambda i:i[2] < 500
filtered = filter(less_than_500,items)
print(f"The output is {filtered}")
# O/P The output is <filter object at 0x0000016935E1AB30>

# Change into list
print(f"\nThe output is {list(filtered)}")

filtered2 : filter(lambda t:t[1][0] == 'P',items)
print(f"\nThe output is {list(filtered2)}")

# ASSIGNMENT QUESTION @6.22.53 hrs



