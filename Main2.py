try:
    num1,num2 = eval(input("Enter two numbers separated by a comma: "))
    result = num1 / num2
    print("The result is:", result)
except ZeroDivisionError as ex:
       print("Error: Division by zero is not allowed.")
       print("Error details:", ex)
except SyntaxError as ex:
       print("Error: Invalid input syntax.")
       print("Error details:", ex)
       print("Please enter the numbers in the correct format. (e.g., 1, 2)")
except:
      print("Wrong input.")
else:
      print("No exceptions")
finally:
      print("This will print no matter what.")

