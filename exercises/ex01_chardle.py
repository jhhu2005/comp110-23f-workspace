"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730664658"

five_char_word: str = input("Enter a 5-character word: ")

if len(five_char_word) != 5:
    print("Error: Word must contain 5 characters.")
    exit()
    
letter: str = input("Enter a single character: ")

if len(letter) != 1:
    print("Error: Character must be a single character.")
    exit()

count: int = 0

print("Searching for " + letter + " in " + five_char_word)

if str(five_char_word[0]) == letter:
    print(letter + " found at index 0")
    count += 1

if str(five_char_word[1]) == letter:
    print(letter + " found at index 1")
    count += 1

if str(five_char_word[2]) == letter:
    print(letter + " found at index 2")
    count += 1

if str(five_char_word[3]) == letter:
    print(letter + " found at index 3")
    count += 1

if str(five_char_word[4]) == letter:
    print(letter + " found at index 4")
    count += 1

if count == 0:
    print("No instances of " + letter + " found in " + five_char_word)

if count == 1:
    print(str(count) + " instance of " + str(letter) + " found in " + five_char_word)

if count == 2:
    print(str(count) + " instances of " + str(letter) + " found in " + five_char_word)







