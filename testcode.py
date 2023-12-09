import unittest
import os
from code import Task, TaskManager

class TestTaskManager(unittest.TestCase):
    def test_add_task(self):
        manager = TaskManager()
        task = Task("Test task", 1)
        manager.add_task(task)
        self.assertEqual(len(manager.tasks), 1)

    def test_get_priority_tasks(self):
        manager = TaskManager()
        task1 = Task("High priority", 3)
        task2 = Task("Low priority", 1)
        manager.add_task(task1)
        manager.add_task(task2)
        priority_1_tasks = manager.get_priority_tasks(1)
        self.assertEqual(len(priority_1_tasks), 1)
        self.assertEqual(priority_1_tasks[0].description, "Low priority")

    def test_save_and_load_tasks(self):
        manager = TaskManager()
        task1 = Task("Task 1", 1)
        task2 = Task("Task 2", 2)
        manager.add_task(task1)
        manager.add_task(task2)

        manager.save_tasks("test_tasks.pkl")

        loaded_manager = TaskManager()
        loaded_manager.load_tasks("test_tasks.pkl")

        self.assertEqual(len(loaded_manager.tasks), 2)
        self.assertEqual(loaded_manager.tasks[0].description, "Task 1")
        self.assertEqual(loaded_manager.tasks[1].priority, 2)

        os.remove("test_tasks.pkl")

if __name__ == "__main__":
    unittest.main()
