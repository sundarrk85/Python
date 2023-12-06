for i in range(1,11):
    print(i)


print(list(range(1,10)))
print(list(range(100,0,-1)))


for i in range(1,11):
    print('\nThe value is {}'.format(i))
else:
    print("\nFor loop is over")


#loop iteration in List
p = [1,2,3,5,9,7,3]
for u in p:
    print('The list item is {}'.format(u))
    print('\nThe square of list item is {}'.format(u**2))