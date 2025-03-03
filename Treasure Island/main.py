print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/____/___
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
direction = input('\tType "left" or "right" : ').lower()

if direction == 'left':
	print('\n\nYou\'ve come to a lake. '
	   		'There is an island in the middle of the lake.'
	   		'\n\tType "wait" to wait for a boat.'
	   		'\n\tType "swim" to swim accross.')
	choice = input("\tYour choice : ").lower()

	if choice == 'wait':
		door = input("\nYou arrived at the island unharmed. There is a house with 3 doors."
			   			"\n\tOne red, one blue, and one yellow."
						"\n\tWhich one would you choose ? : ").lower()
		
		if door == 'red':
			print("\nIt's a room full of fire. Game over :(")
		elif door == 'blue':
			print("\nIt's a room full of beasts. Game over :(")
		elif door == 'yellow':
			print("\nYou found the treasure. You win ! :)")
		else:
			print("\nYou chose a door that does not exist. Game over :(")

	else:
		print("\nYou got attacked by an angry trout. Game over :(")

else:
	print("\nYou fell into a hole. Game over :(")
