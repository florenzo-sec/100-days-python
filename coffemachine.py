

stats = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

drinks = [
    {
        "water": 50,
        "milk": 0,
        "coffee": 18,
        "cost": 1.5,
        "name": "Espresso"
    },
    {
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "cost": 2.5,
        "name": "Latte"
    },
    {
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "cost": 3.0,
        "name": "Cappuccino"
    }
]

def print_options():
    print("Please select a drink:")
    for i in range(len(drinks)):
        drink = drinks[i]
        print(f"{i + 1}. {drink['name']} - ${drink['cost']}")
    print("Type 'report' to view machine resources.")
    print("Type 'off' to turn off the machine.")

def print_report():
    print(f"Water: {stats['water']}ml")
    print(f"Milk: {stats['milk']}ml")
    print(f"Coffee: {stats['coffee']}g")
    print(f"Money: ${stats['money']}")

while True:
    print_options()
    choice = input("Enter the number of your choice: ")
    
    if choice == "off":
        print("Turning off the coffee machine.")
        break
    elif choice == "report":
        print(f"Machine report:\n")
        print_report()
        continue
    elif choice in ["1", "2", "3"]:
        for i in range(len(drinks)):
            if choice == str(i + 1):
                drink = drinks[i]
                for stat in stats:
                    if stat != "money" and drink[stat] > stats[stat]:
                        print(f"Sorry, there is not enough {stat}.")
                        break
                    else:
                        print("Please insert coins.")
                        quarters = int(input("How many quarters?: ")) * 0.25
                        dimes = int(input("How many dimes?: ")) * 0.10
                        nickels = int(input("How many nickels?: ")) * 0.05
                        pennies = int(input("How many pennies?: ")) * 0.01
                        total_inserted = quarters + dimes + nickels + pennies
                        if total_inserted < drink["cost"]:
                            print(f"Sorry, {total_inserted}$ is not enough money. Money refunded.")
                            break
                        else:
                            change = total_inserted - drink["cost"]
                            print((f"Here is ${change} in change.") if change > 0 else 0)
                            for stat in stats:
                                if stat != "money":
                                    stats[stat] -= drink[stat]
                            stats["money"] += drink["cost"]
                            
                            print(f"And here is your {drink['name']}. Enjoy!")
                            break
    else:
        print("Invalid choice. Please try again.")
        continue
                            
                    
                    
                
            