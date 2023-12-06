#STRING
message = "Happy birthday"
name = 'Ram'
quote = '"quote"'
print(quote)


#methods - similar to functions
print(name.upper())              #Print() - func & Upper() - Method
                                # dot - invoking a method

print(name.lower())
print(message.title())
print(message +" "+ name)   #string concatenation
msg = message + " " + name
print("hello \n World")     #hello world                              
print("hello \t world")     #hello  world
print(len(message))
print(message.find('p'))    #if result is -1 then it is not available in str 

print(message.replace('a','5')) #Replace the char

print(message.isalpha())    #returns True if all char are Alphabets else false

print(message.isdigit())    #returns True if all char are digit else false

print(message * 10) #str repetition

#multiple assignments to variables
name, age, height = "John", 23, 178
print(age)

like = dislike = 100    #like = 100, dislike = 100
