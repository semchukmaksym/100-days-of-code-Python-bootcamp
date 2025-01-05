height = float(input("Please enter you height in m:"))
weight = float(input("Please enter you height in kg:"))

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print("Your BMI is underweight")
elif bmi <25:
    print("You have a normal weight")
elif bmi < 30:
    print("Your bmi is overweight")
elif bmi < 35:
    print("Your weight is obese")
else:
    print("Your weight is clinically obese")