from random import choice
from data import data

print("Welcome to the Higher Lower Game")
score = 0
account_a = choice(data)
account_b = choice(data)

while True:
    while account_a == account_b:
        account_b = choice(data)

    print(f"\nCompare A: {account_a['name']}, a {account_a['description']}")
    print("VS")
    print(f"Compare B: {account_b['name']}, a {account_b['description']}\n")

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    if (account_a['followers'] > account_b['followers'] and guess == 'A') or (account_b['followers'] > account_a['followers'] and guess == 'B'):
        score += 1
        print(f"\nYou're right!\n")
        print(f"{account_a['name']} has {account_a['followers']} million followers.")
        print(f"{account_b['name']} has {account_b['followers']} million followers.\n")
        print(f"Current score: {score}.")
        account_a = account_b
        account_b = choice(data)
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        break
    
