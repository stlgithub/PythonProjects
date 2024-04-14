import Art
print(Art.logo)
print("Welcome to Treasue Island!\nYour mission is to find the treasure.")
first_choice = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n")
if first_choice == "right":
    print("You fell into a pit and died. Game over.")
elif first_choice == "left":
    second_choice = input("You arrive at a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
    if second_choice == "swim":
        print("You were eaten by a shark. Game over.")
    elif second_choice == "wait":
        third_choice = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n")
        if third_choice == "red":
            print("You enter a room filled with traps. You died. Game over.")
        elif third_choice == "blue":
            print("You enter a room full of horrible beasts. They eat you alive. Game over.")
        elif third_choice == "yellow":
            print("You found the treasure! You win! ")