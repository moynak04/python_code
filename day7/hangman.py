import random

# Word list
word_list = ["apple", "tiger", "python", "banana", "guitar"]

# Randomly choose a word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Create blanks
display = ["_"] * word_length

# Number of lives
lives = 6

print(" Welcome to Hangman!")

game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

    # Check if already guessed
    if guess in display:
        print(f"You already guessed '{guess}'")

    # Check each letter
    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = guess

    # If guess not in word
    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess! Lives left: {lives}")
        if lives == 0:
            game_over = True
            print(" You lose!")
            print(f"The word was '{chosen_word}'")

    print(" ".join(display))

    # Check win condition
    if "_" not in display:
        game_over = True
        print(" You win!")