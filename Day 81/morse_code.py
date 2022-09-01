# Day 81 of Udemy's 100 Days of Python programming course

# Letters to morse code dictionary.
letters_to_mc = {'a': '.-',
'b': '-...',
'c': '-.-.',
'd': '-..',
'e': '.',
'f': '..-.',
'g': '--.',
'h': '....',
'i': '..',
'j': '.---',
'k': '-.-',
'l': '.-..',
'm': '--',
'n': '-.',
'o': '---',
'p': '.--.',
'q': '--.-',
'r': '.-.',
's': '...',
't': '-',
'u': '..-',
'v': '...-',
'w': '.--',
'x': '-..-',
'y': '-.--',
'z': '--..',
' ': '/',
'1': '.----',
'2': '..---',
'3': '...--',
'4': '....-',
'5': '.....',
'6': '-....',
'7': '--...',
'8': '---..',
'9': '----.',
'0': '-----'}

# Takes a phrase as a text input from the user.
phrase = input("Enter the phrase you wish to translate: ").lower()

# Empty phrase for converted text.
converted_phrase = ''

# For every word in the phrase and every character in each word, take the character and use the conversion
# dictionary to obtain the corresponding value for the character. Append this corresponding value to the 
# converted phrase.
for word in phrase:
    for character in word:
        morse = letters_to_mc[character]
        converted_phrase += (morse)
        converted_phrase += ' '

# Return the converted morse code phrase to the user.
print("Here is your phrase in morse code: " + converted_phrase)