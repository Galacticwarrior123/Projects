def add(p, q):
    return p + q

def subtract(p, q):
    return p - q

def multiply(p, q):
    return p * q

def divide(p,q):
    return p / q

print("Please select the opperation")
print("A. Add")
print("B. Subtract")
print("C. Multiply")
print("D. Divide")  

choice = input("Enter your choice (A/B/C/D): ")
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

if choice == 'A':
    print("Result:", add(num1, num2))
elif choice == 'B':
    print("Result:", subtract(num1, num2))
elif choice == 'C':
    print("Result:", multiply(num1, num2))
elif choice == 'D':
    print("Result:", divide(num1, num2))
else:
    print("Invalid choice")