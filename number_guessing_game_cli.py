"""
Number Guessing Game CLI 

From Roadmap.sh Projects:  https://roadmap.sh/projects/number-guessing-game
"""
import random

random_integer = random.randint(1, 100)
number_of_guesses = 0
intro_loop = True
main_loop = True

print("\nWelcome to the number Guessing Game!"
    "\nI'm thinking of a number between 1 and 100."
    "\nYou have 10, 5 or 3 guesses to find the correct number.")

while intro_loop :
    print('\nWhat difficulty would you like to play?'
        '\n1. Easy - 10 guesses. 2. Medium - 5 guesses. 3. Hard - 3 guesses')
    
    difficulty = int(input("\nEnter 1, 2 or 3: "))
    if difficulty < 1 or difficulty > 3 :
        print("Sorry this is not a valid option")
        break

    options_dict = {
        1 : 'EASY',
        2 : 'MEDIUM',
        3 : 'HARD',
    }
    guesses_dict = {
        'EASY' : 10,
        'MEDIUM' : 5,
        'HARD' : 3,
    }
    print("You chose difficulty:", options_dict[difficulty])
    number_of_guesses = guesses_dict[options_dict[difficulty]]
    break

intro_loop = False

while (number_of_guesses > 0) :   
    print("\nI'm thinking of a number between 1 and 100")
    guess = int(input('What is your guess? '))
    if guess < 1 or guess > 100 :
        print("\nThat is not a valid guess, choose a number between 1 and 100")

    elif guess == random_integer :
        print('\nCongratulations! You guessed the correct number')
        break

    elif guess > random_integer :
        print('\nThat guess is too high')
        number_of_guesses -= 1
        print('You have',number_of_guesses,'guesses remaining')

    elif guess < random_integer :
        print('\nThat guess is too low')
        number_of_guesses -= 1
        print('You have',number_of_guesses,'guesses remaining')

    if number_of_guesses == 0 :
        print("\nSorry you have run out of guesses")
        print("The correct number was", random_integer)
        break   

print("\nGAME OVER")