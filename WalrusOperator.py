name = "Sundar"
print("name")

# using Walrus operator  :=
print(a := "Sundar R K")



print("\nEnter list of numbers. 'z' to exit")
list_num = list() # initialize empty list
while (inp := input()) != 'z':
    list_num.append(int(inp))
print(list_num)