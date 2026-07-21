import math


def show_menu():
    print("Simple Python Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Exit")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please try again.")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ")

        if choice == "6":
            print("Goodbye!")
            break

        if choice not in {"1", "2", "3", "4", "5"}:
            print("Invalid choice. Please try again.")
            continue

        if choice == "5":
            num = get_number("Enter a number: ")
            if num < 0:
                print("Error: Square root of a negative number is not allowed.")
            else:
                result = math.sqrt(num)
                print(f"Result: sqrt({num}) = {result}")
        else:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == "1":
                result = num1 + num2
                print(f"Result: {num1} + {num2} = {result}")
            elif choice == "2":
                result = num1 - num2
                print(f"Result: {num1} - {num2} = {result}")
            elif choice == "3":
                result = num1 * num2
                print(f"Result: {num1} * {num2} = {result}")
            elif choice == "4":
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"Result: {num1} / {num2} = {result}")

        print()


if __name__ == "__main__":
    main()
