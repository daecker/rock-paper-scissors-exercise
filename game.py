# game.py

#imports
import random

#welcome message
print("Rock, Paper, Scissors, Shoot!")

# CAPTURE INPUTS

user_choice = input("Please select Rock, Paper, or Scissors: ")
print("---------")
print("You chose", user_choice)

# VALIDATE INPUTS
options = ["Rock", "Paper", "Scissors"]
if user_choice not in options:
    print("Invalid selection, please try again")
    exit()

# GENERATE COMPUTER SELECTION
#need to create a random selection

computer_choice = random.choice(options)

print("------")
print("Computer Chose: ",computer_choice)

# DETERMINE THE WINNER


# DISPLAY FINAL OUTPUTS / OUTCOMES