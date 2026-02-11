def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial.__doc__)
print("factorial of zero is:", factorial(0))
print("factorial of one is:", factorial(1))
print("factorial of two is:", factorial(2))
print("factorial of three is:", factorial(3))
print("factorial of four is:", factorial(4))
print("factorial of five is:", factorial(5))