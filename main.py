medical_cause = input("Did you have a medical condition? (yes/no) ")
atten=int(input("enter the attendance of the student: "))
if medical_cause == "yes":
    if atten < 75:
        print("You are not eligible for the exam.")
    else:
        print("You are eligible for the exam.")
else:
    if atten < 75:
        print("You are not eligible for the exam.")
    else:
        print("You are eligible for the exam.")