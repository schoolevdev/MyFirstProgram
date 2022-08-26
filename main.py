# This is a sample Python script that puts any number to any exponent.
# This is my first Python Program (it isn't)
# Name: Evin Lodder
# Version/Date: 8/23/2022
import os
import random
import math

choices: list = ["rock", "paper", "scissors"]
win: dict = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}
lose: dict = dict([(value, key) for key, value in win.items()])


def main():
    os.system("cls")
    num: int = random.random()
    while round(num, 12) != 0.999999999999:
        num = random.random()
    print(num)

def main_fun():
    os.system("cls")
    choice: str = input("Rock, paper, or scissors: ").lower()
    if choice not in choices:
        print("That isn't a choice!")
        main()
    computer_choice: str = choices[random.randrange(0, 3)]
    print(f"Computer chose {computer_choice}")

    if win[choice] == computer_choice:
        print("You won!")
    elif lose[choice] == computer_choice:
        print("You lost :(")
    else:
        print("Tie.")
    main()


if __name__ == "__main__":
    main()
