import functools
# reduce(function,iterable) | performs function until one value remains on the iterable
val = [4,7,8,4,3]
# to add all elements 
sum = functools.reduce(lambda x,y:x+y,val)
print(f"The output is {sum}")

chars = ['p','y','t','h','o','n']
word = functools.reduce(lambda a,b:a+b,chars)
print(f"\nThe output is {word}")

# video https://www.youtube.com/watch?v=BiDOehqG68g&t=18450s @6.25.00 hrs

