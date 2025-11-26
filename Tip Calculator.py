print("Welcome to the Tip Calculator")

total = float(input("What was the total bill?\n")) #100
tip_percent = float(input("What percentage tip would you like to give?\n"))#10
people = int(input("How many people to split the bill?\n"))#10

each_pay = (total + total*(tip_percent/100))/people

print("Each person should pay", each_pay)
