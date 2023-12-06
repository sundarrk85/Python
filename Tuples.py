# immuntable | cannot be changed | use ()

tup = (1,2,3)
print(tup)
#tup[0] = 6      # 'tuple' object does not support item assignment

tup = (4,5,2)
print(tup)


# accessing tuple values
print(tup[1])

# index()
print('\nThe index of element 5 is {}'.format(tup.index(5)))

# count()
tup = (11,222,333,4444,4,5,4,5,55,5)
print('\nThe no of times 4 occurs is {}'.format(tup.count(4)))

# for loop
for i in tup:
    print(i)

# isValue in tup
if 333 in tup:
    print('Yes 333 is present in tuple')

if 333 not in tup:
    print('no')

if tup:             # if Tuple is empty, returns false else true
    print('Tuple is not empty')




