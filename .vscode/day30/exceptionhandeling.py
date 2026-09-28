import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary from the CSV
phonetic_dict = {
    row.letter: row.code
    for (index, row) in data.iterrows()
}

word = input("Enter a word: ").upper()

try:
    output = [phonetic_dict[letter] for letter in word]
except KeyError:
    print("Sorry, only letters in the alphabet please.")
else:
    print(output)