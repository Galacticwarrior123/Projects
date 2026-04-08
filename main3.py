import random

class FruitQuiz:
    def __init__(self):
        
        self.fruits = {
            'apple': 'red',
            'banana': 'yellow',
            'orange': 'orange',
            'grape': 'purple',
            'kiwi': 'green'
        }

    def quiz(self):
        while True:
            
            fruit, color = random.choice(list(self.fruits.items()))
            
            print(f"What is the color of {fruit}?")
            user_answer = input("Your answer: ")

            
            if user_answer.lower() == color:
                print("Correct answer")
            else:
                print("Wrong answer")

            
            option = int(input("Do you want to play again? (0 for yes, 1 for no): "))
            if option == 1:
                break

print("Welcome to the Fruit Quiz!")


fq = FruitQuiz()
fq.quiz()