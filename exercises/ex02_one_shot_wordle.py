"""EX02 - One Shot Wordle."""
__author__ = "730664658"

secret_word: str = "python"
guess = input(f"What is your {len(secret_word)}-letter guess? ")
guess_idx = 0
secret_word_idx = 0
emoji: str = ""
exists_anywhere: bool = False

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess) != len(secret_word):
    # Check for if the user's guess is 6 letters
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")
    

# Below checks if user guess is 6 letters then check which letters match
if len(guess) == len(secret_word):
    # If user's guess is less than 6 letters
    while guess_idx < len(secret_word):
        exists_anywhere = False 
        # Exists_anywhere = False serves to reset the search
        # Green box for correctly guessed letters of word and doesn't exist elsewhere
        if guess[guess_idx] == secret_word[secret_word_idx]:
            emoji += GREEN_BOX

        else:
            # If letter doesn't exist anywhere, or exists in another index, results in white box or yellow box
            alternate_idx = 0 
            # Checks if letter exists anywhere else to append a yellow box
            while not exists_anywhere and alternate_idx < len(secret_word):
                if secret_word[alternate_idx] == guess[guess_idx]:
                    exists_anywhere = True
                    emoji += YELLOW_BOX
                alternate_idx += 1
            if not exists_anywhere:
                emoji += WHITE_BOX
        # Runs through next index            
        guess_idx += 1
        secret_word_idx += 1

# Prints the new emoji string
print(emoji)
if secret_word == guess:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")