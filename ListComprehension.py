# To create new list from existing list
# syntax | list_name = [expression for item in iterable] 

# list of square of first 10 natural numbers
sq_list = list(map(lambda x:x*x,range(1,11)))
print(f"The output is {sq_list}")

# using List comprehension
sq_list2 = [x*x for x in range(1,11)]
print(f"\nOutput using List comprehension is {sq_list2}")

temp = [28,30,25,38,22,31]
temp_filtered = [i for i in temp if i<30 ]
print(f"\nOutput using List comprehension is {temp_filtered}")

temp = [28,30,25,38,22,31]
temp_filtered = [i if i<30 else 0 for i in temp]
print(f"\nOutput using List comprehension is {temp_filtered}")
