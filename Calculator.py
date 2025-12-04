
print(r'''    
 _____________________
|  _________________  |
| | PyCalculator!   | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
      ''')

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a /  b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

running = True
n1 = int(input("Enter the first number: "))

while running:

    print("+ | - | * | /")
    operator = input("Enter the operator: ")
    n2 = int(input("Enter the second number:    "))

    if operator in operations:
        result = operations[operator](n1, n2)
        print(f"{n1} {operator} {n2} = {result}")
        n1 = result
    else:
        print("Invalid operator")
    
    cont = input("Do you want to continue with this calculation? Type 'yes' or 'no': ").lower()
    if cont == "no":
        running = False
    else:
        continue
