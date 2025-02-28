import random
from art import logo, stages
from words import word_list


print(logo)
chosen_word = random.choice(word_list)


placeholder = ""
word_len = len(chosen_word)
for letter in range(word_len):
	placeholder += "_ "
print(placeholder)


lives = 6
game_over = False
win_game = False
correct_letters = []


while not game_over:

	display = ""

	guess = input("\n\nGuess a letter : ").lower()

	if guess in correct_letters:
		print("You have guessed the letter.")

	for letter in chosen_word:
		if letter == guess:
			display += letter
			correct_letters.append(guess)

		elif letter in correct_letters:
			display += letter

		else:
			display += "_"

	print(display)

	if guess not in chosen_word:
		print(f"\nYou guessed '{guess}' letter that is not in the word. \nYou lose a life.")
		lives -= 1
		if lives == 0:
			game_over = True


	print(stages[lives])

	if "_" not in display:
		game_over = True
		win_game = True
		print("\nYou win !")

if win_game == False:
	print("\nYou lose :(")
	print(f"The chosen word : {chosen_word}")
	