# Day eight of Udemy's 100 Days of Python programming course

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(text, shift, direction):
    end_text = ""
    if direction == "decode":
            shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {direction}d text is {end_text}")

from art import logo
print(logo)

end = False
while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caeser(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n").lower()
    if restart == "no":
        end = True
        print("Goodbye!")