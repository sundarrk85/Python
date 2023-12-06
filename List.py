cities = ["Chennai","Madurai","Coimbatore","Tirunelveli","Salem","Trichy"]
val = [3,5,6,8,45]
list1 = ["Chennai",3,"Madurai",5.9]

# Accessing list with index
print(cities[-2])
print(val[-2])
print(cities[::2])
print(cities)

# Modify list items
cities[2] = "Tiruchy"
print(cities)

# Append                    Adds item at the last index
cities.append("Karur")
print(cities)

# insert                    Adds item at the specified index
cities.insert(3,"Tanjore")
print(cities)

# Remove using del()        Deletes specified index element   |  it does not return deleted item
del cities[3]               
print(cities)

# pop()                     Deletes "last" element in the list  |   it return the deleted element
deleted = cities.pop()
print('{} has been deleted'.format(deleted))

# pop(index)                Deletes "specified" element in the list  |   it return the deleted element
deleted = cities.pop(2)
print('{} has been deleted'.format(deleted))

# remove                    Removes the values passing from list    
cities.remove("Salem")
print(cities)

# sorting list              Alphabetical(char) or Ascending(int) order
print("\nTemporary Sorting")
print(sorted(cities))       #Sorted - Temporary sort
print('Cities after sorted() function {}'.format(cities))

cities.sort()               # .sort() - Permanent sort


# Reverse
val.reverse()
print('\nValues after reverse {}'.format(val))

# length of the list 
print('\nThe length of the cities is {}'.format(len(cities)))         




