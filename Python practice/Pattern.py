"""
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
"""

rows = int(input('Enter no of rows: '))

for i in range(1,rows + 1):
    for j in range(i):
        print(i,end=' ')
    print('\n')