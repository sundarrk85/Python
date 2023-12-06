TN = ["Madurai","Chennai","Coimbatore","Tirunelveli","Trichy"]

KA = ["Mysore","Bangalore","Udipi"]

AP = ["Tirupati","Nellore","Vijayawada","Guntur"]

# 2d list
India = [TN,KA,AP]

print('This is 2D list\n{}'.format(India))
print('Printing Madurai\n{}'.format(India[0][0]))

a = [1,2,3]
b = a.copy()  # a.copy() or a[:]
print(b)


'''
For copy refer video @2.57 hours
'''

# Deep copy
import copy
Indian_states = copy.deepcopy(India)



