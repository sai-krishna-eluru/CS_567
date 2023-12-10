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
            print(f"Task '{self.tasks[task_index].description}' marked as completed.")
        else:
            print("Invalid task index.")

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

# Example usage
if __name__ == "__main__":
    manager = TaskManager()

    task1 = Task("Complete project", 2)
    task2 = Task("Read a book", 1)
    task3 = Task("Go to the gym", 2)

    manager.add_task(task1)
    manager.add_task(task2)
    manager.add_task(task3)

    while True:
        print("\nTask Manager Menu:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Search Tasks")
        print("5. Save Tasks")
        print("6. Load Tasks")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.display_tasks()
        elif choice == "2":
            description = input("Enter task description: ")
            priority = int(input("Enter task priority: "))
            new_task = Task(description, priority)
            manager.add_task(new_task)
            print("Task added successfully.")
        elif choice == "3":
            task_index = int(input("Enter the index of the task to mark as completed: "))
            manager.mark_task_as_completed(task_index - 1)
        elif choice == "4":
            keyword = input("Enter a keyword to search for tasks: ")
            matching_tasks = manager.search_tasks(keyword)
            print("\nMatching Tasks:")
            for task in matching_tasks:
                print(f"Priority: {task.priority}, Description: {task.description}")
        elif choice == "5":
            filename = input("Enter the filename to save tasks: ")
            manager.save_tasks(filename)
            print("Tasks saved successfully.")
        elif choice == "6":
            filename = input("Enter the filename to load tasks from: ")
            manager.load_tasks(filename)
            print("Tasks loaded successfully.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
