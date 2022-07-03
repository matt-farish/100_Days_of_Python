# Day 26 of Udemy's 100 Days of Python programming course
import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Iterate over the rows in the data and create a dictionary using the letter and code in the row.
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ").upper()

    try:
        # Answer is equal to the value in the phonetic dictionary, using the letter as the key, for each letter in the word.
        answer = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Please use letters only.")
        generate_phonetic()
    else:
        print(answer)


generate_phonetic()