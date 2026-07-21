from pathlib import Path


class TodoList:
    def __init__(self, file_path=None):
        self.file_path = file_path or Path(__file__).resolve().parents[2] / "tasks.txt"
        self.tasks = []
        self.load_tasks()

    def add_task(self, task: str) -> None:
        cleaned_task = task.strip()
        if cleaned_task:
            self.tasks.append(cleaned_task)
            self.save_tasks()

    def view_tasks(self):
        return list(self.tasks)

    def delete_task(self, index: int) -> None:
        if 1 <= index <= len(self.tasks):
            del self.tasks[index - 1]
            self.save_tasks()
        else:
            raise IndexError("Task number does not exist")

    def mark_task_done(self, index: int) -> None:
        if 1 <= index <= len(self.tasks):
            task = self.tasks[index - 1]
            if not task.startswith("[Done] "):
                self.tasks[index - 1] = f"[Done] {task}"
                self.save_tasks()
        else:
            raise IndexError("Task number does not exist")

    def save_tasks(self) -> None:
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        with self.file_path.open("w", encoding="utf-8") as handle:
            for task in self.tasks:
                handle.write(task + "\n")

    def load_tasks(self) -> None:
        if not self.file_path.exists():
            self.tasks = []
            return

        with self.file_path.open("r", encoding="utf-8") as handle:
            self.tasks = [line.strip() for line in handle if line.strip()]
