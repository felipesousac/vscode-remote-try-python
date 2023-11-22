#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

import random

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# create an array of string
def computer_choice_function():
    list = ["rock", "paper", "scissors"]
    return list[random.randint(0, 2)]

# define user choice and counter variables
user_choice = 0
rounds = 0
computer_wins = 0
user_wins = 0

while user_choice != 4:
    # display the menu
    print("=====================================")
    print("Choose one of the following options:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")

    # ask the user for a choice
    user_choice = int(input("Please choose one of the above options: "))

    # if the user enters invalid option it must be handled
    while user_choice < 1 or user_choice > 4:
        print("Invalid option. Please try again.")
        user_choice = int(input("Please choose one of the above options: "))

    # if the user enters 4, then exit the program
    if user_choice == 4:
        print("Thanks for playing!")
        print("You won", user_wins, "rounds.")
        print("The computer won", computer_wins, "rounds.")
        print("There were", rounds, "rounds.")
        break

    # if the user enters 1, 2, or 3, then continue
    if user_choice == 1 or user_choice == 2 or user_choice == 3:
        # call the computer_choice function to get the computer's choice
        computer_choice = computer_choice_function()

        # if the user and computer make the same choice, then it's a tie
        if user_choice == 1 and computer_choice == "rock":
            print("You chose rock and the computer chose rock. It's a tie!")
            rounds += 1
        elif user_choice == 2 and computer_choice == "paper":
            print("You chose paper and the computer chose paper. It's a tie!")
            rounds += 1
        elif user_choice == 3 and computer_choice == "scissors":
            print("You chose scissors and the computer chose scissors. It's a tie!")
            rounds += 1

        # if the user chooses rock and the computer chooses scissors, then the user wins
        elif user_choice == 1 and computer_choice == "scissors":
            print("You chose rock and the computer chose scissors. You win!")
            rounds += 1
            user_wins += 1
        # if the user chooses paper and the computer chooses rock, then the user wins
        elif user_choice == 2 and computer_choice == "rock":
            print("You chose paper and the computer chose rock. You win!")
            rounds += 1
            user_wins += 1
        # if the user chooses scissors and the computer chooses paper, then the user wins
        elif user_choice == 3 and computer_choice == "paper":
            print("You chose scissors and the computer chose paper. You win!")
            rounds += 1
            user_wins += 1

        # if the user chooses rock and the computer chooses paper, then the computer wins
        elif user_choice == 1 and computer_choice == "paper":
            print("You chose rock and the computer chose paper. The computer wins!")
            rounds += 1
            computer_wins += 1
        # if the user chooses paper and the computer chooses scissors, then the computer wins
        elif user_choice == 2 and computer_choice == "scissors":
            print("You chose paper and the computer chose scissors. The computer wins!")
            rounds += 1
            computer_wins += 1
