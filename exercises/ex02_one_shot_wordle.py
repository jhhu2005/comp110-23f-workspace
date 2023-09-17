"""EX02 - One Shot Wordle"""
__author__: "730664658"

secret_word: str = "python"
guess = input (f"What is your {len(secret_word)}-letter guess? ")
guess_idx = 0
secret_word_idx = 0
emoji: str = ""
exists_anywhere: bool = False

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess) != len(secret_word):
    #check for if the user's guess is 6 letters
    guess = input (f"That was not {len(secret_word)} letters! Try again: ")
   
    #if user guess is 6 letters then check if the word is right below

if len(guess) == len(secret_word):
    #if user's guess is 6 letters
    while guess_idx < len(secret_word):
        exists_anywhere = False 
        #exists_anywhere = False serves to reset the search
        #green box for correctly guessed letters of word and doesn't exist elsewhere
        if guess[guess_idx] == secret_word[secret_word_idx]:
            emoji += GREEN_BOX

        else:
            #if letter doesn't exist anywhere, or exists in another index, results in white box or yellow box
            alternate_idx = 0 
            while exists_anywhere==False and alternate_idx < len(secret_word):
                if secret_word[alternate_idx] == guess[guess_idx]:
                    exists_anywhere = True
                    emoji += YELLOW_BOX
                alternate_idx += 1
            if not exists_anywhere:
                emoji += WHITE_BOX
        #runs through next index            
        guess_idx += 1
        secret_word_idx += 1

#prints the new emoji string
print(emoji)
if secret_word == guess:
    print ("Woo! You got it!")
else:
    print ("Not quite. Play again soon!")    

            


   





