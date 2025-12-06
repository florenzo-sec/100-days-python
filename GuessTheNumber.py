from random import randint
print("Welcome to Guess The Number!")
print("I'm thinking of a number between 1 and 100.")

number_to_guess = randint(1, 100)
def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    else:
        print("Invalid difficulty selected. Defaulting to 'easy'.")
        attempts = 10
    
    print(f"You have {attempts} attempts to guess the number.")
    return attempts

attempts = set_difficulty()

user_guess = int(input("Make a guess: "))

def check_answer(guess, answer):
    if guess < answer:
        return "Too low."
    elif guess > answer:
        return "Too high."
    else:
        return f"You got it! The answer was {answer}."

while attempts > 0:
    result = check_answer(user_guess, number_to_guess)
    print(result)
    if user_guess == number_to_guess:
        break

    attempts -= 1
    if attempts == 0:
        print("You've run out of guesses. You lose.")
        print(f"The number was {number_to_guess}.")
        break
    else:
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))

    
