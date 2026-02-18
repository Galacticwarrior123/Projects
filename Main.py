try:
    number = int(input("Enter a number: "))
except ValueError as ex:
    print("Invalid input. Please enter a valid number.")
    print("Error details:", ex)