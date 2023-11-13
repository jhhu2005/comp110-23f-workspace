"""EX03 - Structured Wordle."""
__author__ = "730664658"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(main_string: str, search_char: str) -> bool:
    """Searches for character in string."""
    assert len(search_char) == 1
    main_string_idx: int = 0
    # Returns true if the single character is found anywhere in the main string, if not return false.
    while main_string_idx < len(main_string):
        if search_char == main_string[main_string_idx]:
            return True
        else:
            main_string_idx += 1 
    return False 


def emojified(guess: str, secret: str) -> str:
     """Creates string of emoji."""
    assert len(guess) == len(secret)
    emoji: str = ""
    secret_idx: int = 0
    guess_idx: int = 0
    # Adds the box that corresponds to whether the current character of index is matching, existing in string, or not existing at all.
    while (int(guess_idx)) < len(secret):
        if secret[secret_idx] == guess[guess_idx]:
            emoji += GREEN_BOX
        else: 
            if contains_char(secret, guess[guess_idx]):
                emoji += YELLOW_BOX
            else: 
                emoji += WHITE_BOX
        guess_idx += 1
        secret_idx += 1
    return emoji


def input_guess(input_guess_len: int) -> str:
    """Prompts for user input."""
    # Asks for user input and returns if matches the expected string length.
    guess: str = input("Enter a " + str(input_guess_len) + " character word: ")
    while input_guess_len != len(guess):
        guess = input("That wasn't " + str(input_guess_len) + " chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn_number: int = 0
    won: bool = False
    
    # Loops through the turn numbers and stops loop if turns goes above 6.
    while turn_number < 6 and (not won):
        turn_number += 1
        print("=== Turn " + str(turn_number) + "/6 ===")
        # Calls input_guess function
        guess: str = input_guess(5)
        # Calls emojified function to display correct characters/existing/wrong characters.
        print(emojified(guess, "codes"))
        if guess == "codes":
            won = True
    if won:
        print("You won in " + str(turn_number) + "/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()