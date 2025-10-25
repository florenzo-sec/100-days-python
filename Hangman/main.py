import random
from stages import lives

word_list = ["python", "java", "kotlin", "javascript"]

chosen_word = random.choice(word_list)
print(chosen_word) # For testing purposes, to see the chosen word


placeholder = ""
for letter in chosen_word:
    placeholder += "_"

game_over = False
correct_letters = []
lives_index = 0

while not game_over:
    guess = input("Guess a letter: ").lower()

    # Check if the letter is in the chosen word using a for loop
    if guess in chosen_word:
        correct_letters.append(guess)
    else:
        print("Letter not in word.")
        lives_index += 1
    
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += guess
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)
    try:    
        print(lives[lives_index])
    except IndexError:
        print("Game over")
        game_over = True

    if display == chosen_word:
        print("You win!")
        game_over = True