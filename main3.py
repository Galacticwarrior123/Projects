print("Select Your ride")
print("1. Bike")
print("2. Car")

choice = int(input("Enter your choice: "))

if(choice==1):
   print("What type of bike")
   print("1. Sports Bike")
   print("2. Cruiser Bike")
   print("3. Dirt Bike")
   bike_choice = int(input("Enter your choice: "))
   if(bike_choice==1):
       print("You have selected Sports Bike")
   elif(bike_choice==2):
       print("You have selected Cruiser Bike")
   elif(bike_choice==3):
       print("You have selected Dirt Bike")
   else:
       print("Invalid choice")

elif(choice==2):
   print("What type of car")
   print("1. Sedan")
   print("2. SUV")
   print("3. Hatchback")
   car_choice = int(input("Enter your choice: "))
   if(car_choice==1):
       print("You have selected Sedan")
   elif(car_choice==2):
       print("You have selected SUV")
   elif(car_choice==3):
       print("You have selected Hatchback")
   else:
       print("Invalid choice")
