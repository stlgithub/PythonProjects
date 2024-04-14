height = float(input())

weight = int(input())

bmi = weight / (height*height)

if bmi >= 35:
  print(f"Your BMI is {bmi}, you are clinically obese.")
elif bmi >= 30:
  print(f"Your BMI is {bmi}, you are obese.")
elif bmi >= 25:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi >= 18.5:
  print(f"Your BMI is {bmi}, you have a normal weight.")
else:
  print(f"Your BMI is {bmi}, you are underweight.")