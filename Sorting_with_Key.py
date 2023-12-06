cities = ["Madurai","Chennai","Coimbatore","Tirunelveli"]
# Permanent sort
cities.sort()
print(f'Cities after permanently sorted using "sort()" method {cities}')

# Temporary sort
val = [5,9,1,2,4,5]
print(f'\nVal after temporarily sorted using "sorted()" function {sorted(val)}')
print(f'\nVal is {val}')



# (itemcode, itemname, price)
# items = list of tuples
items = [(3456,"Shoe",780),(3556,"Phone",21000),(2587,"Book",450),(5412,"Pen",75)]
items.sort()
print(f'\nIt will sort by using Itemcode if we call items.sort() {items}')
print(f'\nBut the requirement is to sort using Itemname or price. To do this\n')
items.sort(key=lambda i:i[1])       # i is the iterator | i[1] is the index of itemname
print(f'\nSorted using itemname key {items}')

items.sort(key=lambda i:i[2])       # i is the iterator | i[2] is the index of price | Default = asc order
print(f'\nSorted using price key {items}')

items.sort(key=lambda i:i[2],reverse=True)       # Desc order
print(f'\nSorted using price key {items}')





# tuple of tuples --> We can't use sort() method because it is immutable in nature
# but we can use sorted() function for temporary sort
items2 = ((3456,"Shoe",780),(3556,"Phone",21000),(2587,"Book",450),(5412,"Pen",75))
print(f'\nitems2 after using sorted() {sorted(items2)}')
print(f'\noriginal tuple {items2}')







