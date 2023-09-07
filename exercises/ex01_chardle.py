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

#variable for counting instances
count: int = 0

print("Searching for " + letter + " in " + five_char_word)

#if the character at index matches the input letter then the program will state the input is found at that index and the count will go up by 1
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

#if no instances were found then it will state no instances of the letter are found in the word, or else it will state how many instances of the letter were found
if count == 0:
    print("No instances of " + letter + " found in " + five_char_word)
#if 1 instance was found
if count == 1:
    print(str(count) + " instance of " + str(letter) + " found in " + five_char_word)
#if 2 instances were found
if count == 2:
    print(str(count) + " instances of " + str(letter) + " found in " + five_char_word)







