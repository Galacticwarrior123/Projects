import random

while True:
    user_action = input("Enter a choice (rock,paper,scissors): ")

    possible_actions = ["rock", "paper", "scissors"]

    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n" )

    if user_action == computer_action:
        print("It's a tie!")
    elif user_action == "rock":
        if computer_action == "paper":
            print("Paper covers rock. You lose!")
        else:
            print("Rock crushes scissors. You win!")
    elif user_action == "paper":
        if computer_action == "scissors":
            print("Scissors cut paper. You lose!")
        else:
            print("Paper covers rock. You win!")
    elif user_action == "scissors":
        if computer_action == "rock":
            print("Rock crushes scissors. You lose!")
        else:
            print("Scissors cut paper. You win!")
