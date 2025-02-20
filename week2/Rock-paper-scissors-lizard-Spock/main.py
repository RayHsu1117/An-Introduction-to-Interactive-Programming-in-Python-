# Rock-paper-scissors-lizard-Spock template
import random


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "wrong input"
    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "wrong input"

    # convert number to a name using if/elif/else
    # don't forget to return the result!


def rpsls(player_choice):
    # delete the following pass statement and fill in your code below
    print("\n")
    # print a blank line to separate consecutive games
    print("Player chooses "+player_choice)
    # print out the message for the player's choice
    name_to_number(player_choice)
    # convert the player's choice to player_number using the function name_to_number()
    comp_number = random.randrange(0,5)
    # compute random guess for comp_number using random.randrange()
    computer_choice = number_to_name(comp_number)
    # convert comp_number to comp_choice using the function number_to_name()
    print("Computer chooses "+computer_choice)
    # print out the message for computer's choice
    if player_choice == "rock":
        if computer_choice == ("scissors" or "lizard"):
            print("Player wins!")
        elif computer_choice == "rock":
            print("Player and computer tie!")
        else:
            print("Computer wins!")
    if player_choice == "paper":
        if computer_choice == ("rock" or "Spock"):
            print("Player wins!")
        elif computer_choice == "paper":
            print("Player and computer tie!")
        else:
            print("Computer wins!")
    if player_choice == "scissors":
        if computer_choice == ("paper" or "lizard"):
            print("Player wins!")
        elif computer_choice == "scissors":
            print("Player and computer tie!")
        else:
            print("Computer wins!")
    if player_choice == "Spock":
        if computer_choice == "scissors" or "rock":
            print("Player wins!")
        elif computer_choice == "Spock":
            print("Player and computer tie!")
        else:
            print("Computer wins!")
    if player_choice == "lizard":
        if computer_choice == ("paper" or "Spock"):
            print("Player wins!")
        elif computer_choice == "lizard":
            print("Player and computer tie!")
        else:
            print("Computer wins!")
    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message


# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
