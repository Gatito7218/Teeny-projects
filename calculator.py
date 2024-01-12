def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


print("Please select operation: \n"
      "1. Add \n"
      "2. Subtract \n"
      "3. Multiply \n"
      "4. Divide \n")

while True:
    select = input("Enter choice(1/2/3/4): ")
    if select in ('1', '2', '3', '4'):
        try:
            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if select == '1':
            print(f"{n1:,} + {n2:,} = {add(n1, n2):,}")

        elif select == '2':
            print(f"{n1:,} - {n2:,} = {subtract(n1, n2):,}")

        elif select == '3':
            print(f"{n1:,} * {n2:,} = {multiply(n1, n2):,}")

        elif select == '4':
            print(f"{n1:,} / {n2:,} = {divide(n1, n2):,}")
    
        next_calculation = input("Another calculation? (yes/no): ") 
        if next_calculation in ("yes", "no"):
            if next_calculation == "yes":
                continue
            else:
                break
        else:
            print("Enter a valid input")
            continue
    else:
        print("Invalid Input")
