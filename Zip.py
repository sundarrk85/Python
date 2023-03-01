# zips 2 or more iterables into one
items = ['phone','lamp','table','pen']
price = [25000,2500,5200,15]
zipped = zip(items,price)
print(f"The output is {zipped}")
# The output is <zip object at 0x000001702B2FDE80>

zipped = list(zip(items,price))
print(f"The output is {zipped}")
