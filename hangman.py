import random

# A list of simple words to pick from (predefined words requirement)
words = ["python", "software", "alpha", "intern", "laptop"]

# Pick one word at random
secret_word = random.choice(words)

# Set up tracking variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("=== Welcome to Hangman! ===")

# Keep playing until 6 wrong guesses are reached
while incorrect_guesses < max_attempts:
    # 1. Build the visible word (letters or blanks)
    display = ""
    for char in secret_word:
        if char in guessed_letters:
            display += char + " "
        else:
            display += "_ "
    
    print("\nWord: " + display)
    print("Wrong guesses left:", max_attempts - incorrect_guesses)
    
    # 2. Check if the player won
    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word correctly!")
        break

    # 3. Take letter input from user
    guess = input("Enter a letter: ").lower().strip()

    # Simple validations
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter only.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    # Add the guess to our tracked list
    guessed_letters.append(guess)

    # 4. Check if the letter is in the secret word
    if guess in secret_word:
        print("Good job! That letter is in the word.")
    else:
        incorrect_guesses += 1
        print("Wrong letter!")

# 5. Check if the player lost
if incorrect_guesses == max_attempts:
    print("\n💀 Game over! You ran out of tries.")
    print("The word was:", secret_word)