# map(function, iterable) | func - Normal func or lamba func
items = [(3456,"Shoe",780),(3556,"Phone",21000),(2587,"Book",450),(5412,"Pen",75)]

# want to convert item[2] into USD so divided by 74
inr_usd = lambda i:(i[0],i[1],i[2]/74)   
items_usd = list(map(inr_usd,items))
inr_usd2 = lambda i:(i[0],i[1],float("{:.2f}".format(i[2]/74))) 
items_usd2 = list(map(inr_usd2,items))

print(f"The output without .2f is {items_usd}")
print(f"\nThe output with .2f is {items_usd2}")

val = [4,5,1,9,7]
val_sq = map(lambda x:x*x, val)
print(f"\nThe output is {val_sq}")
# O/P The output is <map object at 0x000001D120B3BE50>
# We have to store it as a list 
val_sq = list(map(lambda x:x*x, val))
print(f"\nThe output is {val_sq}")


# Map using normal function
def sq_fun(x):
    return x*x
var_sq = list(map(sq_fun,val))
print(f"\nThe output using normal function is {val_sq}")







