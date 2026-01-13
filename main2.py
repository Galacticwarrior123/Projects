actual_cost = float(input("Enter the actual cost of the item: "))
sale_amount = float(input("Enter the sale amount: "))

if (sale_amount < actual_cost):
    amount = sale_amount - actual_cost
    print("Total profit:", amount)
else:
    amount = actual_cost - sale_amount
    print("Total loss:", amount)