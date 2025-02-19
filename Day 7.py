# --------------------------- Project --------------------------------
# Hangman
# --------------------------------------------------------------------

# -------------------------- Objectives ------------------------------
# Understanding for & while loops, if & else, lists, strings, range
# --------------------------------------------------------------------


import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========''']

word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

print(r'''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')

chosen_word = random.choice(word_list)


placeholder = ""
word_len = len(chosen_word)
for letter in range(word_len):
	placeholder += "_ "
print(placeholder)


game_over = False
lives = 6
corrent_letters = []

while not game_over:

	display = ""

	guess = input("\n\nGuess a letter : ").lower()

	if guess in corrent_letters:
		print("You have guessed the letter.")

	for letter in chosen_word:
		if letter == guess:
			display += letter
			corrent_letters.append(guess)

		elif letter in corrent_letters:
			display += letter

		else:
			display += "_"

	print(display)

	if guess not in chosen_word:
		print(f"\nYou guessed '{guess}' letter that is not in the word. \nYou lose a life.")
		lives -= 1
		if lives == 0:
			game_over = True
			print("\nYou lose :(")
			print(f"The chosen word : {chosen_word}")

	print(stages[lives])

	if "_" not in display:
		game_over = True
		print("\nYou win !")
