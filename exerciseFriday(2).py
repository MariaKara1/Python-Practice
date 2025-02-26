#program that generates random number and has user guess what it is
import random

random_num=random.randint(0,100)
guess_count = 0

while True:
    guess = int(input("Guess a number! \n"))
    if guess < random_num:
        print("The random number is higher!")
        guess_count = guess_count + 1
    elif guess > random_num:
        print("The random number is lower!")
        guess_count = guess_count + 1
    else:
        guess_count = guess_count + 1
        print("Yay! You guessed it! You used a total of", guess_count, "guesses!")
        break
