Height=float(input("Enter height in centimeters: "))
Weight=float(input("Enter weight in kilograms: "))

BMI=Weight/(Height/100) ** 2
print("Your BMI is: ", BMI)

if BMI<18.4:
    print("You are underweight.")
elif BMI<24.9:
    print("You have a normal weight.")
elif BMI<=29.9:
    print("You are serverly overweight.")
elif BMI<=34.9:
    print("You are obese.")
else:
    print("You are obese.")
    