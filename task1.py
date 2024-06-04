import random

while True:
    print("********************************************************")
    print("*              Rock-Paper-Scissors Game                *")
    print("********************************************************")
    
    user_input = input("Enter a choice (rock, paper, scissors): ")
    available_inputs = ["rock", "paper", "scissors"]
    computer_inputs = random.choice(available_inputs)
    print(f"\nYou chose {user_input}, computer chose {computer_inputs}.\n")

    if user_input == computer_inputs:
        print(f"Both players selected {user_input}. It is a tie!")
    elif user_input == "rock":
        if computer_inputs == "scissors":
            print("Rock smashes scissors! You won the game!")
        else:
            print("Paper covers the rock! you lost the game.")
    elif user_input == "paper":
        if computer_inputs == "rock":
            print("Paper covers the rock! you won the game!")
        else:
            print("scissors cuts the paper! You lost the game.")
    elif user_input == "scissors":
        if computer_inputs == "paper":
            print("scissors cuts the paper! You won the game!")
        else:
            print("rock smashes the scissors! You lost the game.\n")

    play_again = input("want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break
