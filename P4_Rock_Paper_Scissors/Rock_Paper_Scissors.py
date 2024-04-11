import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_options = [rock, paper, scissors]
computer_choice = computer_options[random.randint(0,2)]
print(computer_choice)
if player_choice == 0:
  if computer_choice == rock:
    print("Draw!")
  elif computer_choice == paper:
    print("You lose!")
  elif computer_choice == scissors:
    print("You win!")
elif player_choice == 1:
  if computer_choice == rock:
    print("You win!")
  elif computer_choice == paper:
    print("Draw!")
  elif computer_choice == scissors:
    print("You lose!")
elif player_choice == 2:
  if computer_choice == rock:
    print("You lose!")
  elif computer_choice == paper:
    print("You win!")
  elif computer_choice == scissors:
    print("Draw!")
else:
  print("Invalid input. Restart the game.")