import unittest
import io
import os
import contextlib
from code import Task, TaskManager, TaskStatistics, TaskFormatter, TaskLogger, TaskValidator, TaskExecutor, TaskScheduler, TaskAssigner, TaskReporter

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

    def test_remove_completed_tasks(self):
        task1 = Task("Completed task", 1)
        task1.completed = True
        task2 = Task("Incomplete task", 2)
        self.manager.add_task(task1)
        self.manager.add_task(task2)

        self.assertEqual(len(self.manager.tasks), 2)
        self.manager.remove_completed_tasks()
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0].description, "Incomplete task")

    def test_display_tasks(self):
        task1 = Task("Display task", 2)
        self.manager.add_task(task1)

        expected_output = "1. Priority: 2, Description: Display task, Status: Pending\n"

        with io.StringIO() as captured_output:
            with contextlib.redirect_stdout(captured_output):
                self.manager.display_tasks()

            self.assertEqual(captured_output.getvalue(), expected_output)

    def test_get_high_priority_tasks(self):
        task1 = Task("High priority", 3)
        task2 = Task("Low priority", 1)
        task3 = Task("Another high priority", 3)
        self.manager.add_task(task1)
        self.manager.add_task(task2)
        self.manager.add_task(task3)

        high_priority_tasks = self.manager.get_high_priority_tasks()
        self.assertEqual(len(high_priority_tasks), 2)
        self.assertEqual(high_priority_tasks[0].description, "High priority")
        self.assertEqual(high_priority_tasks[1].description, "Another high priority")

    def test_update_task_description(self):
        task = Task("Old description", 1)
        self.manager.add_task(task)
        self.manager.update_task_description(0, "New description")
        self.assertEqual(self.manager.tasks[0].description, "New description")

class TestTaskStatistics(unittest.TestCase):
    def test_task_statistics(self):
        manager = TaskManager()
        task_stats = TaskStatistics(manager)

        task1 = Task("Task 1", 1)
        task2 = Task("Task 2", 2)
        task3 = Task("Task 3", 3)
        manager.add_task(task1)
        manager.add_task(task2)
        manager.add_task(task3)

        self.assertEqual(task_stats.count_tasks(), 3)

        task1.completed = True
        task2.completed = True
        self.assertEqual(task_stats.count_completed_tasks(), 2)
        self.assertEqual(task_stats.count_pending_tasks(), 1)

class TestTaskFormatter(unittest.TestCase):
    def test_format_task(self):
        formatter = TaskFormatter()
        task = Task("Formatted task", 2)
        formatted_task = formatter.format_task(task)
        self.assertEqual(formatted_task, "Description: Formatted task, Priority: 2, Completed: False")

class TestTaskLogger(unittest.TestCase):
    def test_log_task(self):
        logger = TaskLogger()
        task = Task("Logged task", 1)
        with self.assertLogs(level="INFO"):
            logger.log_task(task)

class TestTaskValidator(unittest.TestCase):
    def test_validate_task(self):
        validator = TaskValidator()
        valid_task = Task("Valid task", 2)
        validator.validate_task(valid_task)

        invalid_task = Task("", 0)
        with self.assertRaises(ValueError):
            validator.validate_task(invalid_task)

class TestTaskExecutor(unittest.TestCase):
    def test_execute_task(self):
        executor = TaskExecutor()
        task = Task("Task to execute", 3)

        with warnings.catch_warnings(record=True) as warning_list:
            warnings.simplefilter("always")  # Capture all warnings
            executor.execute_task(task)

            self.assertTrue(any(isinstance(w.message, UserWarning) for w in warning_list))

class TestTaskScheduler(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()
        self.scheduler = TaskScheduler()

    def test_schedule_task(self):
        task = Task("Task to schedule", 2)
        self.manager.add_task(task)
        
        initial_tasks_count = len(self.manager.tasks)
        self.scheduler.schedule_task(task)
        scheduled_tasks_count = len(self.manager.get_priority_tasks(2))

        self.assertEqual(scheduled_tasks_count, 1)
        self.assertEqual(initial_tasks_count, scheduled_tasks_count + 1)

class TestTaskAssigner(unittest.TestCase):
    def test_assign_task(self):
        assigner = TaskAssigner()
        task = Task("Task to assign", 2)

        with self.assertWarns(UserWarning):
            assigner.assign_task(task)

class TestTaskReporter(unittest.TestCase):
    def test_report_task(self):
        reporter = TaskReporter()
        task = Task("Task to report", 1)

        with self.assertWarns(UserWarning):
            reporter.report_task(task)

if __name__ == "__main__":
    unittest.main()
