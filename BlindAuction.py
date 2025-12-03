print(r'''                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      / _______________\'''')

import os

print("Welcome to the Blind Auction!")
bids = {}

def get_bidder():
    name = input("What is your name?: ")
    price = float(input("What is your bid?: $"))
    bids[name] = price
    
while True:
    get_bidder()
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if more_bidders.strip() == 'no':
        break
    os.system('cls' if os.name == 'nt' else 'clear')

for bidder in bids:
    if bids[bidder] == max(bids.values()):
        print(f"The winner is {bidder} with a bid of ${bids[bidder]:.2f}!")

