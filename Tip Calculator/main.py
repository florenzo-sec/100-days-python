
print("Welcome to the Tip Calculator!")

bill_amount = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

number_of_people = int(input("How many people to split the bill? "))

tip_amount = bill_amount * (tip_percentage / 100)
total_bill = bill_amount + tip_amount

amount_per_person = total_bill / number_of_people

print(f"Each person should pay: ${amount_per_person}")