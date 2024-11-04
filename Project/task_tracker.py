import sys
import json
import os
from datetime import datetime

TASKS_FILE = 'tasks.json'

# Load tasks from the JSON file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

# Save tasks to the JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks) + 1  
    new_task = {
        'id': task_id,
        'description': description,
        'status': 'todo',
        'createdAt': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added: {description}")

# Update a task's description
def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            save_tasks(tasks)
            print(f"Task {task_id} updated.")
            return
    print(f"Task with ID {task_id} not found.")

# Delete a task
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f"Task {task_id} deleted.")

# Change the status of a task
def change_status(task_id, new_status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = new_status
            save_tasks(tasks)
            print(f"Task {task_id} marked as {new_status}.")
            return
    print(f"Task with ID {task_id} not found.")

# List all tasks
def list_tasks(status_filter=None):
    tasks = load_tasks()
    if status_filter:
        tasks = [task for task in tasks if task['status'] == status_filter]
    if tasks:
        for task in tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['createdAt']}")
    else:
        print("No tasks found.")

# Main function to handle commands
def main():
    if len(sys.argv) < 2:
        print("Usage: python task_tracker.py <command> [<args>]")
        return

    command = sys.argv[1]

    if command == "add":
        description = " ".join(sys.argv[2:])
        add_task(description)
    elif command == "update":
        task_id = int(sys.argv[2])
        new_description = " ".join(sys.argv[3:])
        update_task(task_id, new_description)
    elif command == "delete":
        task_id = int(sys.argv[2])
        delete_task(task_id)
    elif command == "mark":
        task_id = int(sys.argv[2])
        new_status = sys.argv[3]
        change_status(task_id, new_status)
    elif command == "list":
        if len(sys.argv) > 2:
            list_tasks(sys.argv[2])
        else:
            list_tasks()
    else:
        print("Unknown command.")

if __name__ == "__main__":
    main()
