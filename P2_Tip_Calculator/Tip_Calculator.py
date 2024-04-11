print("Welcome to the tip calculator!")
total = float(input("What was the total bill?\n$"))
tip = float(input("How much tip would you like to give?\n"))
people = float(input("How many people to split the bill?\n"))
amount_pay = (total + total * (tip / 100)) / people
print(f"Each person should pay: ${round(amount_pay, 2)}")