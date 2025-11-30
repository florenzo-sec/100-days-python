from random import randint

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
ascii_arts = [rock, paper, scissors]

print("Welcome to the Rock Paper Scissors game!")

choices =  ["Rock", "Paper", "Scissors"]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))
computer_choice = randint(0,2)

for i in range(0,3):
    if i == user_choice:
        print(f"You chose {choices[i]}")
        print(ascii_arts[i])
        print(f"Computer chose {choices[computer_choice]}")
        print(ascii_arts[computer_choice])

        if computer_choice == user_choice:
            print("It's a tie!")
        else:
            if (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0):
                print("You lost!")
            else:
                print("You won!")





