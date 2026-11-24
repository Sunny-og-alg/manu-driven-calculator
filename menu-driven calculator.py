"""PS 28 - Menu-Driven Calculator (Python 3)"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b          # raises ZeroDivisionError if b == 0


def power(a, b):
    return a ** b


def modulus(a, b):
    return a % b          # raises ZeroDivisionError if b == 0


# choice -> (symbol, function)
OPERATIONS = {
    1: ("+", add),
    2: ("-", subtract),
    3: ("*", multiply),
    4: ("/", divide),
    5: ("^", power),
    6: ("%", modulus),
}


def show_menu():
    print("\n===== MENU-DRIVEN CALCULATOR =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7. Exit")


def main():
    while True:
        show_menu()

        # Validate menu choice
        try:
            choice = int(input("Enter your choice (1-7): ").strip())
        except ValueError:
            print("Invalid choice. Select 1 to 7.")
            continue

        if choice == 7:
            print("Thank you for using the calculator. Exiting...")
            break

        if choice not in OPERATIONS:
            print("Invalid choice. Select 1 to 7.")
            continue

        # Read numbers and compute
        try:
            a = float(input("Enter first number: ").strip())
            b = float(input("Enter second number: ").strip())

            symbol, func = OPERATIONS[choice]
            result = func(a, b)

            if isinstance(result, complex):
                print("Error: Result is not a real number.")
                continue

            print(f"{a:g} {symbol} {b:g} = {result:.2f}")

        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except ValueError:
            print("Invalid number. Enter numeric values only.")
        except OverflowError:
            print("Error: Result is too large.")


if __name__ == "__main__":
    main()







