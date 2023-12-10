import pickle

class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.completed = False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_priority_tasks(self, priority):
        return [task for task in self.tasks if task.priority == priority and not task.completed]

    def get_completed_tasks(self):
        return [task for task in self.tasks if task.completed]

    def mark_task_as_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True

    def search_tasks(self, keyword):
        return [task for task in self.tasks if keyword.lower() in task.description.lower()]

    def display_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "Completed" if task.completed else "Pending"
            print(f"{i + 1}. Priority: {task.priority}, Description: {task.description}, Status: {status}")

    def save_tasks(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.tasks, file)

    def load_tasks(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.tasks = pickle.load(file)
        except FileNotFoundError:
            print("File not found. No tasks loaded.")
        except Exception as e:
            print(f"An error occurred while loading tasks: {e}")

    def remove_completed_tasks(self):
        self.tasks = [task for task in self.tasks if not task.completed]

    def get_high_priority_tasks(self):
        return [task for task in self.tasks if task.priority == 3]

    def update_task_description(self, task_index, new_description):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].description = new_description

# Additional functionality
class TaskStatistics:
    def __init__(self, task_manager):
        self.task_manager = task_manager

    def count_tasks(self):
        return len(self.task_manager.tasks)

    def count_completed_tasks(self):
        return len(self.task_manager.get_completed_tasks())

    def count_pending_tasks(self):
        return self.count_tasks() - self.count_completed_tasks()
