import datetime
import os
import json
import sys

def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            return json.load(file)
    else:
        return []
    
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:  # Corrected 'W' to 'w' for write mode
        json.dump(tasks, file, indent=4)

def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    created_at = updated_at = datetime.datetime.now().isoformat()  # Corrected datetime usage

    new_task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": created_at,
        "updatedAt": updated_at
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")

def update_task(task_id, new_description):
    tasks = load_tasks()
    
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.datetime.now().isoformat()  # Corrected datetime usage
            save_tasks(tasks)
            print(f"Task ID {task_id} updated successfully.")
            return
    
    print(f"Task ID {task_id} not found.")

def delete_task(task_id):
    tasks = load_tasks()
    
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print(f"Task ID {task_id} deleted successfully.")

def mark_in_progress(task_id):
    tasks = load_tasks()
    
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            task["updatedAt"] = datetime.datetime.now().isoformat()  # Corrected datetime usage
            save_tasks(tasks)
            print(f"Task ID {task_id} marked as in-progress.")
            return
    
    print(f"Task ID {task_id} not found.")

def mark_done(task_id):
    tasks = load_tasks()
    
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            task["updatedAt"] = datetime.datetime.now().isoformat()  # Corrected datetime usage
            save_tasks(tasks)
            print(f"Task ID {task_id} marked as done.")
            return
    
    print(f"Task ID {task_id} not found.")

def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task["status"] == status]
    
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['createdAt']}, Updated At: {task['updatedAt']}")

def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [arguments]")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "add":
        description = " ".join(sys.argv[2:])
        add_task(description)
    
    elif command == "update":
        task_id = int(sys.argv[2])
        description = " ".join(sys.argv[3:])
        update_task(task_id, description)
    
    elif command == "delete":
        task_id = int(sys.argv[2])
        delete_task(task_id)
    
    elif command == "mark-in-progress":
        task_id = int(sys.argv[2])
        mark_in_progress(task_id)
    
    elif command == "mark-done":
        task_id = int(sys.argv[2])
        mark_done(task_id)
    
    elif command == "list":
        if len(sys.argv) == 3:
            list_tasks(sys.argv[2])  # List tasks by status
        else:
            list_tasks()  # List all tasks
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()
