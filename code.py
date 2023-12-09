import pickle

class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_priority_tasks(self, priority):
        return [task for task in self.tasks if task.priority == priority]

    def display_tasks(self):
        for task in self.tasks:
            print(f"Priority: {task.priority}, Description: {task.description}")

    def save_tasks(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.tasks, file)

    def load_tasks(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.tasks = pickle.load(file)
        except FileNotFoundError:
            print("File not found. No tasks loaded.")

# Example usage
if __name__ == "__main__":
    manager = TaskManager()

    task1 = Task("Complete project", 2)
    task2 = Task("Read a book", 1)
    task3 = Task("Go to the gym", 2)

    manager.add_task(task1)
    manager.add_task(task2)
    manager.add_task(task3)

    manager.display_tasks()

    priority_2_tasks = manager.get_priority_tasks(2)
    print("\nPriority 2 tasks:")
    for task in priority_2_tasks:
        print(f"Description: {task.description}")

    manager.save_tasks("tasks.pkl")
    manager.load_tasks("tasks.pkl")

    print("\nAfter loading tasks:")
    manager.display_tasks()
