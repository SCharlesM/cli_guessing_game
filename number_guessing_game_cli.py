"""
Number Guessing Game CLI 

From Roadmap.sh Projects:  https://roadmap.sh/projects/number-guessing-game
"""
import random

random_integer = random.randint(1, 100)
loop = True

print('Welcome to the number Guessing Game!)
print("I'm thinking of a number between 1 and 100.")
print("You have 3, 5 or 10 guesses to find the correct number.")

while(loop):

