print("Welcome to Alen's BMI calculator 2.0!!!")
name = input(str("What is your name?\n"))
print("Hello " + name +"," + " let's find out your bmi")
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi= round((weight/height**2))
if bmi <18.5 :
    print(f"Your BMI is {bmi}, you are are underweight.")
elif 18.5<=bmi <25 :
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif 25<=bmi <30 :
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif 30<=bmi <35 :
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi>35:
    print(f"Your BMI is {bmi}, you are clinically obese.")