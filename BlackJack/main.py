from random import choice
from os import system,name
from title import title

print(title)

cards_dict = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 11
}

def deal_card():
    """Returns a random card from the deck."""
    cards = list(cards_dict.keys())
    return choice(cards)
def calculate_score(hand):
    """Calculates the score of a given hand."""
    score = sum(cards_dict[card] for card in hand)
    if score == 21 and len(hand) == 2:
        return 0  # Blackjack
    if 'A' in hand and score > 21:
        # Change Ace from 11 to 1
        score = sum(cards_dict[card] for card in hand)-10
    return score

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack!"
    elif user_score == 0:
        return "Win with a Blackjack!"
    elif user_score > 21:
        return "You busted out. You lose!"
    elif computer_score > 21:
        return "Opponent busted out. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_hand = []
    computer_hand = []
    is_game_over = False

    for _ in range(2):
        user_hand.append(deal_card())
        computer_hand.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_hand)
        computer_score = calculate_score(computer_hand)
        print(f"   Your cards: {user_hand}, current score: {user_score}")
        print(f"   Computer's first card: {computer_hand[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_hand.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    print(f"   Your final hand: {user_hand}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_hand}, final score: {computer_score}")
    print(compare(user_score, computer_score))
    
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    system('cls' if name == 'nt' else 'clear')
    play_game()