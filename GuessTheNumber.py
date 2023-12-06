import random

num = random.randint(1,20)    # Generates random number between 1 and 20
guess = int(input("Can you guess the number I am thinking? It's less than 20 : "))

while num!=guess:
    if guess > num:
        print("Your guess is higher\n")
    else:
        print("Your guess is lower\n")
    guess = int(input("Guess again : "))
print("You won!")

