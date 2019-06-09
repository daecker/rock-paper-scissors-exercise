### DE INCLASS game.py
#
##imports
#import random
#
##welcome message
#print("Rock, Paper, Scissors, Shoot!")
#
## CAPTURE INPUTS
#
#user_choice = input("Please select Rock, Paper, or Scissors: ")
#print("---------")
#print("You chose:", user_choice)
#
## VALIDATE INPUTS
#options = ["Rock", "Paper", "Scissors"]
#if user_choice not in options:
#    print("Invalid selection, please try again")
#    exit()
#
## GENERATE COMPUTER SELECTION
##need to create a random selection
#
#computer_choice = random.choice(options)
#
#print("------")
#print("Computer Chose: ",computer_choice)
#
## DETERMINE THE WINNER
##Rock > Scissors; Paper > Rock; Scissors > Paper
##Same = Tie
#
#if user_choice == computer_choice:
#    print("It's a tie!")
#
#elif user_choice == "Rock" and computer_choice =="Paper":
#    print("Paper is the winner")
#elif user_choice == "Rock" and computer_choice =="Scissors":
#    print("Rock is the winner")
#
#elif user_choice == "Paper" and computer_choice =="Rock":
#    print("Rock is the winner")
#elif user_choice == "Paper" and computer_choice =="Scissors":
#    print("Scissors is the winner")
#
#elif user_choice == "Scissors" and computer_choice =="Rock":
#    print("Rock is the winner")
#elif user_choice == "Scissors" and computer_choice =="Paper":
#    print("Scissors is the winner")
#
#
## DISPLAY FINAL OUTPUTS / OUTCOMES

# PROFESSOR'S  game.py

import random

def my_message(): ##creating function for the purpose of testing
    return "HELLO" 

def determine_winner(user_choice, computer_choice):
    winners = {
        "rock":{
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper":{
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors":{
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        },
    }
    winning_choice = [user_choice] [computer_choice]
    return winning_choice

#use this for testing purposes. it means if this script is executed from the command-line
if __name__ == "__main__":
        

    print("Rock, Paper, Scissors, Shoot!") # this is also a comment

    # CAPTURE INPUTS

    user_choice = input("Please choose one of the following options: 'rock', 'paper', or 'scissors' (without the quotes):")

    print("--------------")
    print("USER CHOICE:", user_choice)

    # VALIDATE INPUTS

    options = ["rock", "paper", "scissors"]

    if user_choice not in options:
        print("INVALID SELECTION, PLEASE TRY AGAIN...")
        exit()

    # GENERATE COMPUTER SELECTION

    computer_choice = random.choice(options)

    print("--------------")
    print("GENERATING...")
    print("COMPUTER CHOICE:", computer_choice)

    # DETERMINE THE WINNER
    #
    # rock beats scissors
    # paper beats rock
    # scissors beats paper
    # same selections is a tie
    #
    # first attribute represents the user, second represents the computer
    winners = {
        "rock":{
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper":{
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors":{
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        },
    }

    winning_choice = winners[user_choice][computer_choice]

    # DISPLAY FINAL OUTPUTS / OUTCOMES

    if winning_choice:
        if winning_choice == user_choice:
            print("YOU WON")
        elif winning_choice == computer_choice:
            print("YOU LOST")
    else:
        print("TIE")

    print("Thanks for playing. Please play again!")