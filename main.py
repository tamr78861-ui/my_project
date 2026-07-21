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
