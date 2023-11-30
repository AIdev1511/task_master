import json
from datetime import datetime, timedelta



class Task:
    def __init__(self, description, due_date=None, completed=False):
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def __str__(self):
        return f'{self.description} (Due: {self.due_date.strftime("%Y-%m-%d") if self.due_date else "N/A"}) - {"Completed" if self.completed else "Pending"}'


class TaskMaster:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date_str):
        try:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

        new_task = Task(description, due_date)
        self.tasks.append(new_task)
        print(f'Task "{description}" added successfully!')

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            print(f'Task "{self.tasks[task_index].description}" marked as completed!')
        else:
            print('Invalid task index. Please try again.')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks available.')
        else:
            print('Task List:')
            for i, task in enumerate(self.tasks):
                print(f'{i + 1}. {task}')

    def save_tasks_to_file(self, filename='tasks.json'):
        with open(filename, 'w') as file:
            task_list = [{'description': task.description, 'due_date': task.due_date.strftime("%Y-%m-%d") if task.due_date else None, 'completed': task.completed} for task in self.tasks]
            json.dump(task_list, file)
        print(f'Tasks saved to {filename}.')

    def load_tasks_from_file(self, filename='tasks.json'):
        try:
            with open(filename, 'r') as file:
                task_list = json.load(file)
                self.tasks = [Task(task['description'], datetime.strptime(task['due_date'], "%Y-%m-%d") if task['due_date'] else None, task['completed']) for task in task_list]
            print(f'Tasks loaded from {filename}.')
        except (FileNotFoundError, json.JSONDecodeError):
            print(f'No tasks found in {filename}.')


def run_taskmaster():
    task_master = TaskMaster()

    while True:
        print("\nNamaste! Welcome to TaskMaster by Jatin:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. View Tasks")
        print("4. Save Tasks to File")
        print("5. Load Tasks from File")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            description = input("Enter task description: ")
            due_date_str = input("Enter due date (YYYY-MM-DD), leave blank if none: ")
            task_master.add_task(description, due_date_str)
        elif choice == '2':
            task_index = int(input("Enter task index to mark as completed: ")) - 1
            task_master.mark_task_completed(task_index)
        elif choice == '3':
            task_master.view_tasks()
        elif choice == '4':
            task_master.save_tasks_to_file()
        elif choice == '5':
            task_master.load_tasks_from_file()
        elif choice == '6':
            print('Exiting TaskMaster. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 6.')


if __name__ == "__main__":
    run_taskmaster()
# code by jatin Pandey