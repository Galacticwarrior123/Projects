class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return f"{self.word} ( {self.meaning} )"

flash = []

print("Welcome to the flashcard application")

while True:
    word = input("Enter the word: ")
    meaning = input("Enter the meaning: ")

    flash.append(flashcard(word, meaning))

    option = int(input("Enter 0 to continue, 1 to stop: "))
    
    if option == 1:
        break

print("\nYour flashcards")

for i in flash:
    print(">", i)