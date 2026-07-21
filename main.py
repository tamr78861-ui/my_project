from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from simple_project.todo import TodoList


def main() -> None:
    todo = TodoList(Path(__file__).resolve().parent / "tasks.txt")

    print("Simple To-Do List")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Mark task as done")
    print("5. Quit")

    while True:
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            task = input("Enter a task: ").strip()
            todo.add_task(task)
            print("Task added.")
        elif choice == "2":
            tasks = todo.view_tasks()
            if tasks:
                print("Your tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
            else:
                print("No tasks yet.")
        elif choice == "3":
            tasks = todo.view_tasks()
            if not tasks:
                print("No tasks to delete.")
                continue

            print("Your tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                number = int(input("Enter the task number to delete: "))
                todo.delete_task(number)
                print("Task deleted.")
            except ValueError:
                print("Please enter a valid number.")
            except IndexError as exc:
                print(exc)
        elif choice == "4":
            tasks = todo.view_tasks()
            if not tasks:
                print("No tasks to mark as done.")
                continue

            print("Your tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                number = int(input("Enter the task number to mark as done: "))
                todo.mark_task_done(number)
                print("Task marked as done.")
            except ValueError:
                print("Please enter a valid number.")
            except IndexError as exc:
                print(exc)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please choose a valid option.")


if __name__ == "__main__":
    main()

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
