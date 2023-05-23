import random

# generate a random number between 1 and 1000
secret_number = random.randint(1, 1000)

# initialize the number of guesses
num_guesses = 10

# loop until the user guesses the number or runs out of guesses
while num_guesses :
    # prompt the user for a guess
    guess = input("Guess the secret number (between 1 and 1000): ")
    try:
        guess = int(guess) if guess >0 and guess<1000
    except ValueError:
        print("Invalid input! Please enter an integer between 1 and 1000.")
        continue
        
    # check if the guess is correct
    if guess == secret_number:
        print("Congratulations, you guessed the secret number!")
        break
    elif guess < secret_number:
        print("The secret number is higher than your guess.")
    else:
        print("The secret number is lower than your guess.")
        
    # increment the number of guesses
    num_guesses -= 1

# check if the user has used up all their guesses
if num_guesses == 0:
    print("Sorry, you ran out of guesses. The secret number was", secret_number)
