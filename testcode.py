import unittest
import os
from code import Task, TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = Task("Test task", 1)
        self.manager.add_task(task)
        self.assertEqual(len(self.manager.tasks), 1)

    def test_get_priority_tasks(self):
        task1 = Task("High priority", 3)
        task2 = Task("Low priority", 1)
        self.manager.add_task(task1)
        self.manager.add_task(task2)
        priority_1_tasks = self.manager.get_priority_tasks(1)
        self.assertEqual(len(priority_1_tasks), 1)
        self.assertEqual(priority_1_tasks[0].description, "Low priority")

    def test_mark_task_as_completed(self):
        task = Task("Incomplete task", 2)
        self.manager.add_task(task)
        self.manager.mark_task_as_completed(0)
        self.assertTrue(self.manager.tasks[0].completed)

    def test_search_tasks(self):
        task1 = Task("Read a book", 2)
        task2 = Task("Write a book", 1)
        self.manager.add_task(task1)
        self.manager.add_task(task2)
        matching_tasks = self.manager.search_tasks("book")
        self.assertEqual(len(matching_tasks), 2)
        self.assertEqual(matching_tasks[0].priority, 2)
        self.assertEqual(matching_tasks[1].priority, 1)

    def test_save_and_load_tasks(self):
        task1 = Task("Task 1", 1)
        task2 = Task("Task 2", 2)
        self.manager.add_task(task1)
        self.manager.add_task(task2)

        self.manager.save_tasks("test_tasks.pkl")

        loaded_manager = TaskManager()
        loaded_manager.load_tasks("test_tasks.pkl")

        self.assertEqual(len(loaded_manager.tasks), 2)
        self.assertEqual(loaded_manager.tasks[0].description, "Task 1")
        self.assertEqual(loaded_manager.tasks[1].priority, 2)

        os.remove("test_tasks.pkl")

# MutPy requires a simple test function for mutation testing
def test_simple():
    assert 1 + 1 == 2

if __name__ == "__main__":
    unittest.main()
