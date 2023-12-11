# Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

list_a = [10,20,25,35,47,20]
list_b = [80,44,45,13,12,14]
final_list = []
for i in list_a:
    # odd number from list_a
    if int(i) % 2 != 0:
        final_list.append(i)

for i in list_b:
    # even number from list_b
    if int(i) % 2 == 0:
        final_list.append(i)
result = final_list.sort()
print(f'\nThe final list befpre sorting: {final_list}\nThe final list is {result} ')