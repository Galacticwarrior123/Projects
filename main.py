import random
import time

number = random.randint(1, 100)

def intro():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")
    name = input("What's your name? ")
    if (number%2==0):
        x = "even"
    else:
        x = "odd"
    print("\nThis is {} number.".format(x))
    time.sleep(.5)
    print("Go ahead . Guess!")

def pick():
    guessesTaken = 0
    while guessesTaken < 6:
        time.sleep(.25)
        enter = input("Enter your guess: ")
        try:
            guess = int(enter)
            if guess <= 100 and guess >= 1:
                guessesTaken = guessesTaken + 1
            if guessesTaken < 6:
                if guess < number:
                    print("Your guess is too low.")
                if guess > number:
                    print("Your guess is too high.")
                if guess != number:
                    time.sleep(.5)
                    print("Try again.")
                if guess == number:
                    break
            if guess > 100 or guess < 1:
                    print("Please enter a number between 1 and 100.")
                    time.sleep(.25)
                    print("Try again.")
        except:
            print("Please enter a valid number.")
    if guess == number:
        guessesTaken = str(guessesTaken)
        print("Congratulations! You guessed the number in {} tries.".format(guessesTaken))
    if guess != number:
        print("Sorry, you didn't guess the number. The number was {}.".format(number))

playagain = "yes"
while playagain == "yes" or playagain == "y" or playagain == "Yes":
    intro()
    pick()
    playagain = input("Do you want to play again?")