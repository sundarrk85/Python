for i in range(1,6):
    print(i, end='')        # end = '' prints all items in single line

print('')                   # Prints empty line - \n or ''
print("This is nested loop")
for h in range(1,4):           # controls rows
    for i in range(1,6):       # controls columns
        print(i, end='')
    print('')


