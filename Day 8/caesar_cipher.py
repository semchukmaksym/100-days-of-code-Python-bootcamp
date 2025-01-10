import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    lower_orig = original_text.lower()

    if encode_or_decode == "decode":
        shift_amount *= -1

    encrypted = ""
    for letter in lower_orig:
        if letter not in alphabet:
            encrypted += letter
        else:
            encrypted_index = alphabet.index(letter) + shift_amount
            encrypted += alphabet[encrypted_index]
    print(f"Here is {encode_or_decode}ed result: {encrypted}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type you message:\n")
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'")
    if restart == 'no':
        should_continue = False
        print("Good bye")