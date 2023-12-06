# Get a list of numbers and add them to list

print("Enter the Numbers. Enter Z to exit\n")
k = []

while True:    # Don't know the times the loops should run. so I will tell when shiuld it stop.
    inp = input()
    if inp == 'z' or inp == 'Z':
        break                               # break --> stops the current loop 
    else:
        k.append(int(inp))
print(k)


# continue  -  Remove "," from string
str = "a,b,c,d,e,f,g,"
str2 = ''
for i in str:
    if i == ",":
        continue                            # continue - if it encounters comma then it will move on to next iteration
    else:
        str2 = str2 + i
print(str2)



# pass - instead of leaving blank we can use pass. Edhuvum panna vendam next line ku poiru
