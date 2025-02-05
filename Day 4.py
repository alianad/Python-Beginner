# --------------------- Project ------------------------------
# Rock Paper Scissors Game
# ------------------------------------------------------------

# --------------------- Objectives ---------------------------
# Understanding randomisation and python lists
# ------------------------------------------------------------

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
---'    ____)____
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

art = [rock, paper, scissors]

print("\nWhat do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissor")
user_choice = int(input("\nYour choice : "))

if user_choice >= 3 or user_choice < 0:
	print("\nYou typed an invalid number. You lose ! :(")

else:
	print(art[user_choice])

	computer_choice = random.randint(0, 2)
	print(f"\nComputer chose : \n{art[computer_choice]}\n")

	if user_choice == computer_choice:
		print("It's a draw.")
	elif user_choice == 0:
		if computer_choice == 1:
			print("You lose !")
		else:
			print("You win !")
	elif user_choice == 1:
		if computer_choice == 0:
			print("You win !")
		else:
			print("You lose !")
	elif user_choice == 2:
		if computer_choice == 0:
			print("You lose !")
		else:
			print("You win !")
