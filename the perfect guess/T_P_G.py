# We are going to write a program that generates a random number and asks the user to
# guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower
# number please”. Similarly, if the user’s guess is too low, the program prints “higher
# number please” When the user guesses the correct number, the program displays the
# number of guesses the player used to arrive at the number.
# Hint: Use the random module.

import random

computer=random.randint(1,10)

user=0

guess=0

while(computer!=user):
    user=int(input("enter any number between 1 and 10: "))

    if(user>10 or user<1):
        print("please enter number between 1 and 10")
    guess +=1
    if(computer>user):
        print("higher number please")
    elif(computer<user):
        print("lower number please")

print(f"the number was {computer} and you find in {guess} attempt")