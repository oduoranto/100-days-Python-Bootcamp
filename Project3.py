print("Welcome to the BMI calculato")
height = float(input("What is your height: "))
weight = int(input("Enter your weight: "))
bmi = weight/(height*height)

if bmi < 18.5:
    print("You are underweight")
elif bmi < 25: 
    print("You are normal")
elif bmi < 30:
    print("You are slightly overweight")
elif bmi < 35:
    print("You are obese")
else:
    print("You are clinically obese")        

               