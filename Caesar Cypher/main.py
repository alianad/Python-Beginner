from art import logo

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"\nHere is the {encode_or_decode}d result: \n\t{output_text}")
    print("\n----------------------------------------------------------\n")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

game_continue = True

while game_continue:

    print("\n----------------------------------------------------------\n")

    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n\t").lower()
    text = input("Type your message:\n\t").lower()
    shift = int(input("Type the shift number:\n\t"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n\t")

    if choice == 'no':
        game_continue = False
