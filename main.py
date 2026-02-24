import random 
playing = True
number = str(random.randint(0,9))
print ("I will generate a number from 1 to 9,and you have to guess one digit at a time")
print("The game ends when you get 1 hero!")
while playing:
    guess = input("Enter your guess:")
    if guess == number:
        print("Congratulations! You guessed the number.")
        playing = False
    else:
        print("Sorry, try again.")