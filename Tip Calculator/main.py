
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
bill_tot_person = bill / people + (bill * tip_percentage / 100) / people
print(f"Each person should pay: ${bill_tot_person}")