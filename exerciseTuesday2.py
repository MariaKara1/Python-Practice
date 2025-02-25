import random
import time

#function to generate a wheel
def generate_wheel():
    spaces = []
    for i in range(18):
        spaces.append("red")
        spaces.append("black")
    for i in range(2):
        spaces.append("green")
    return spaces

#function to reutrn a random space landed on
def spin_wheel(spaces):
    return random.choice(spaces)

#function that lets user gamble on roulette spins
def play_game():
    money = 10000
    spaces = generate_wheel()

    while True:
        print("You have $" +  str(money) +  ".")
        bet = input("How much do you want to bet?\n")
        bet = int(bet)
        color = input("What color do you want to bet on?\n")

        print("The wheel is spinning. Good luck!")
        time.sleep(2)
        landed = spin_wheel(spaces)
        print("It landed on " + landed + ".")

        if landed == color:
            money = money + bet
            print("Congratulations! You now have $" + str(money) + "!")
        else:
            money = money - bet
            print("Sorry! You now have $" + str(money))

        play_again = input("Do you want to play again? \n")
        if play_again == "no":
            break
play_game()