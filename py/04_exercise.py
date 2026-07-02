# Write a program that categorizes BMI (Body mass index) into
# underweight(<18.5), normal weight(<24.9), overweight(<29.9),
# and obesity(>30.0). (formula = kg/m^2, where kg is a person's weight 
# in kilograms and m^2 is their height in meters squared)



weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))

bmi = weight / ((height / 100) ** 2)

if bmi < 18.5:
    print("You are underweight. Your BMI is {:.2f}".format(bmi))
if bmi < 24.9:
    print("You have a normal weight. Your BMI is {:.2f}".format(bmi))
if bmi < 29.9:
    print("You are overweight. Your BMI is {:.2f}".format(bmi))
if bmi > 30.0:
    print("You are obese. Your BMI is {:.2f}".format(bmi))