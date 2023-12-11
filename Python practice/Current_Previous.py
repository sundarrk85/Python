# Print current and prev number and their sum in range of 10

for i in range(10):
    if i == 0:
        print(f'The current number is {i} and previous number is {i} and their sum is {i+i}')
    else:
        print(f'The current number is {i} and previous number is {i-1} and their sum is {i+(i-1)}')   
    