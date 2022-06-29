# Day 26 of Udemy's 100 Days of Python programming course
import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Iterate over the rows in the data and create a dictionary using the letter and code in the row.
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()

# Answer is equal to the value in the phonetic dictionary, using the letter as the key, for each weather in the word.
answer = [phonetic_dict[letter] for letter in word]

print(answer)