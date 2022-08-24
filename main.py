# This is a sample Python script that puts any number to any exponent.
# This is my first Python Program (it isn't)
# Name: Evin Lodder
# Version/Date: 8/23/2022
import os
import random
def main():
    os.system("cls")
    choice: str = input("Rock, paper, or scissors: ").lower()
    computerchoice: str = random.random(["rock", "paper", "scissors"])
    match choice:
        case "rock":
            if computerchoice == "scissors":
                print("You won!")
            elif computerchoice == "paper":
                print("You lost :(")
            else: print("Tie.")
            pass
        case "paper":
            if computerchoice == "rock":
                print("You won!")
            elif computerchoice == "scissors":
                print("You lost :(")
            else:
                print("Tie.")
            pass
        case "scissors":
            if computerchoice == "paper":
                print("You won!")
            elif computerchoice == "rock":
                print("You lost :(")
            else:
                print("Tie.")
            pass
        case _:
            print("That isn't rock, paper, or scissors!")
            pass
    main()


if __name__ == "__main__":
    main()
