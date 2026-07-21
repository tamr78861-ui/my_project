import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from simple_project.todo import TodoList


class TodoListTests(unittest.TestCase):
    def test_add_and_view_tasks(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "tasks.txt"
            todo = TodoList(path)
            todo.add_task("Buy milk")
            self.assertEqual(todo.view_tasks(), ["Buy milk"])

    def test_delete_task(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "tasks.txt"
            todo = TodoList(path)
            todo.add_task("Buy milk")
            todo.add_task("Walk dog")
            todo.delete_task(1)
            self.assertEqual(todo.view_tasks(), ["Walk dog"])

    def test_save_and_load_tasks(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "tasks.txt"
            todo = TodoList(path)
            todo.add_task("Read book")
            todo.save_tasks()

            loaded = TodoList(path)
            loaded.load_tasks()
            self.assertEqual(loaded.view_tasks(), ["Read book"])


if __name__ == "__main__":
    unittest.main()
