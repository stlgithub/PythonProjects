import art

print(art.logo)

def add(number_one,number_two):
  return number_one + number_two

def subtract(number_one,number_two):
  return number_one - number_two

def multiply(number_one,number_two):
  return number_one * number_two

def divide(number_one,number_two):
  return number_one / number_two
  
def calculator():
  number_one = int(input("What's the first number?: "))
  print("+\n-\n*\n/")
  operation = input("Pick an operation: ")
  number_two = int(input("What's the next number?: "))
  answer = 0
  if operation == "+":
    answer = add(number_one,number_two)
  elif operation == "-":
    answer = subtract(number_one,number_two)
  if operation == "*":
    answer = multiply(number_one,number_two)
  if operation == "/":
    answer = divide(number_one,number_two)
  print(f"{number_one} {operation} {number_two} = {answer}")

calculator()