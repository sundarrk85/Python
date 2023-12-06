# key value pair

user = {
    'name' : "Sundar",
    'age' : 25,
    'gender' : 'male'
}

print("\nThe user's gender is {}".format(user['gender']))

# Adding new key value pair
user['city'] = "Chennai"
print("\nThe Dictionary after added city key is {}".format(user))

# Modify
user['age'] = 26
print("\nThe Dictionary after modified age key is {}".format(user))

# delete 
del user['gender']
print("\nThe Dictionary after deleted gender key is {}".format(user))

# looping                           # it doesn't care about order
for key,val in user.items():
    print("Key is {}".format(key))
    print("Value is {}".format(val))

# looping only keys
for key in user.keys():
    print("Key is {}".format(key))

# display keys in sorted order
for key in sorted(user.keys()):
    print(key)
    print('The value of {} is {}'.format(key,user[key]))    # getting values --> user[key]


job = {'Priya':'CTS','Nivetha':'Amazon','Aiswarya':'Google'}
for company in job.values():
    print(company)

'''

* Can't repeat keys
* values can be similar
* user.items() --> to loop through keys and values
* user.keys() --> to loop through keys only
* user.values() --> to loop through values only

'''

# list of dictionaries 
users = []
user = {'name':"Ram",'age':25,'gender':'male'}
users.append(user)
print("\nThe list after adding user dict is {}".format(users))

user = {'name':"Ramya",'age':24,'gender':'female'}
users.append(user)
print("\nThe list after adding user dict is {}".format(users))

print(users[0])
print(users[1])
print(users[1]['age'])

# list in dictionary
user['fav_food'] = ['Lemon rice','Chapati','Poori']
print("\nThe list after adding fav_food to dict is {}".format(user))
print(user['fav_food'][1])









