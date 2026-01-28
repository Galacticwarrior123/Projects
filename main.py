string = input("Enter your string: ")

char = input("Enter the character you are looking for :")

i = 0

count = 0

while (i < len(string)):
    if (string[i] == char):
        count += 1
    i += 1
print("The character", char, "appears", count, "times in the string.")
