# game.py

#imports
import random

#welcome message
print("Rock, Paper, Scissors, Shoot!")

# CAPTURE INPUTS

user_choice = input("Please select Rock, Paper, or Scissors: ")
print("---------")
print("You chose:", user_choice)

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
#Rock > Scissors; Paper > Rock; Scissors > Paper
#Same = Tie

if user_choice == computer_choice:
    print("It's a tie!")

elif user_choice == "Rock" and computer_choice =="Paper":
    print("Paper is the winner")
elif user_choice == "Rock" and computer_choice =="Scissors":
    print("Rock is the winner")

elif user_choice == "Paper" and computer_choice =="Rock":
    print("Rock is the winner")
elif user_choice == "Paper" and computer_choice =="Scissors":
    print("Scissors is the winner")

elif user_choice == "Scissors" and computer_choice =="Rock":
    print("Rock is the winner")
elif user_choice == "Scissors" and computer_choice =="Paper":
    print("Scissors is the winner")


# DISPLAY FINAL OUTPUTS / OUTCOMES