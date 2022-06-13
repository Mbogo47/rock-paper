import random


options = ["R", "S", "P"]

computer_option = random.choice(options)

choice = input("What do you choose? Type R for Rock, P for Paper, S for Scissors.\n").upper()

while choice == computer_option:
    choice = input("What do you choose? Type R for Rock, P for Paper, S for Scissors.\n").upper()
if choice == "R" and computer_option == "S":
    print(f"Player ({choice}) : Computer({computer_option})")
    print("You Win")
elif choice == "P" and computer_option == "R":
    print(f"Player ({choice}) : Computer({computer_option})")
    print("You Win!")
elif choice == "S" and computer_option == "P":
    print(f"Player ({choice}) : Computer({computer_option})")
    print("You Win!")
elif choice not in options:
    print(f"Player ({choice}) : Computer({computer_option})")
    print("You typed an invalid option")
else:
    print(f"Player ({choice}) : Computer({computer_option})")
    print("You Lose!")

