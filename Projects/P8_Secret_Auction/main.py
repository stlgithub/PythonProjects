import os

import art
bidders = {}

print(art.logo)
print("Welcome to the secret auction program.")
def accept_bid():
  name = input("What is your name?: ")
  bid = input("What's your bid?: $")
  bidders[name] = int(bid)
  default_bid = 0
  default_bidder = ""
  for key in bidders:
    if bidders[key] > default_bid:
      default_bidder = key
      default_bid = bidders[key]
  others = input("Are there any other bidders? Type 'yes or 'no'")
  if others == "yes":
    #clear()
    os.system('cls')
    accept_bid()
  else:
    print(f"The winner is {default_bidder} with a bid of ${default_bid}")

accept_bid()