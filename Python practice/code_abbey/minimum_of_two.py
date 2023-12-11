no_of_items = int(input('Enter no of list items: '))
myList1=[]
myList2=[]
final_list=[]

# Getting list items from user
if no_of_items > 0:
    print('************List 1 items*************')
    for i in range(1,no_of_items + 1):
        list_item=int(input(f'Enter item {i}: \n'))
        myList1.append(list_item)

    print('************List 2 items*************')
    for j in range(1,no_of_items + 1):
        list_item=int(input(f'Enter item {j}: \n'))
        myList2.append(list_item)
else:
    print('No of list items should be greater than 0')


# addition logic
print(f'List 1: {myList1}\nList 2: {myList2}\n')
for item in range(no_of_items):
    final_list.append(min(myList1[item],myList2[item]))

# Result
print(f'The final result is {final_list}')