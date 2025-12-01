from asciiarts import HANGMANPICS
from requests import get
from random import choice

print(r'''   
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')

print("Welcome to Hangman! Guess the animal name.")

DB_SIZE = 1000
URL = f"https://api.datamuse.com/words?ml=animal&max={DB_SIZE}" 
#the DB's animal names are kinda strange, you might get some weird words
#i suggest changing the API to get better names

try:
    response = get(URL)
    word = choice(response.json())['word']
except Exception as e:
    print(f"Error fetching word from API: {e}")
    word = "elephant"  # fallback word

display = []
for _ in range(len(word)):
    display += "_"
print("Word to guess: "+" ".join(display))

lives = 6
end_of_game = False
guessed_letters = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You've already guessed the letter '{guess}'.")
    else:
        guessed_letters.append(guess)

        for position in range(len(word)): 
            letter = word[position] #takes the letter at the current position
            if letter == guess:
                display[position] = letter

        if guess not in word:
            lives -= 1
            print(f"The letter '{guess}' is not in the word. You lose a life.")
            if lives == 0:
                end_of_game = True
                print("You lose. The word was: " + word)

    print(" ".join(display))
    print(HANGMANPICS[6 - lives])

    if "_" not in display:
        end_of_game = True
        print("You win!")
    