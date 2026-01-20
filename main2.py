units = int(input("Enter the number of units consumed: "))

if (units > 50):
    amount = units * 2.50
    surcharge = 25
elif (units > 100):
    amount = units * 3.70
    surcharge = 35
elif (units > 150):
    amount = units * 4.25
    surcharge = 45
elif(units > 200):
    amount = units * 5
    surcharge = 50
else:
    amount = 0
    surcharge = 0

total_amount = amount + surcharge
print("Total amount to be paid:", total_amount)