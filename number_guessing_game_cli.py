"""
Number Guessing Game CLI 

From Roadmap.sh Projects:  https://roadmap.sh/projects/number-guessing-game
"""
import random

random_integer = random.randint(1, 100)
number_of_guesses = 0
intro_loop = True
main_loop = True

print('\nWelcome to the number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")
print("You have 10, 5 or 3 guesses to find the correct number.")

while intro_loop:
    print('\nWhat difficulty would you like to play?')
    print('1. Easy 10 guesses\n2. Medium 5 guesses\n3. Hard 3 guesses')

    difficulty = int(input('\nEnter 1, 2, or 3: '))
    if difficulty in ('1', '2', '3') :
    #if difficulty in range(1, 3) :
        match difficulty :
            case '1' :
                print('You chose difficulty EASY')
                number_of_guesses = 10
                break
            case '2' :
                print('You chose difficulty MEDIUM')
                number_of_guesses = 5
                break
            case '3' :
                print('You chose difficulty HARD')
                number_of_guesses = 3
                break
    else:
        print('\nSorry that is not a valid option')
intro_loop = False

while (number_of_guesses > 0) :   
    print("\nI'm thinking of a number between 1 and 100")
    guess = int(input('What is your guess? '))
    if guess == random_integer :
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
print("\nGAME OVER")