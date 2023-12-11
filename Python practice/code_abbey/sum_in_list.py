no_of_items = int(input('Enter no of list items: '))
myList=[]

# Getting list items from user
if len(no_of_items) > 0:
    for i in range(1,no_of_items + 1):
        list_item=int(input(f'Enter item {i}: \n'))
        myList.append(list_item)
else:
    print('No of list items should be greater than 0')

# Addition logic
sum=0;
for item in myList:
    sum+=item
print(f'The sum of list items is {sum}')
 