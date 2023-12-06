"""
str="Happy"
to print
H                   y
Ha                  py
Hap                 ppy
Happ                appy
Happy               Happy
"""

str = "Happy"
print('{}\n{}\n{}\n{}\n{}\n'.format(str[0],str[0:2],str[0:3],str[0:4],str[0:5]))
print('{}\n{}\n{}\n{}\n{}'.format(str[-1],str[-2:],str[-3:],str[-4:],str[-5:]))

