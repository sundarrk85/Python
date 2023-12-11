# Display numbers divisible by 5 from a list
a = [26,5,69,15,25,34,50]

for i in a:
    if int(i)%5 == 0:
        print(f'{i} is divisible by 5 and its index value is {a.index(i)}')
        