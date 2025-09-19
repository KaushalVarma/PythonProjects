# PythonProjects - Task Tracker CLI

Task tracker is a project used to track and manage your tasks. This is a simple command line interface (CLI) to track what you need to do, what you have done, and what you are currently working on.

Project URL: "https://roadmap.sh/projects/task-tracker"

## Features

- Add new tasks
- List all tasks or filter by status
- Update task descriptions
- Delete tasks
- Mark tasks as todo, in-progress, or done
- Persistent storage using JSON

## Installation

No external dependencies required. Uses only Python standard library.

```bash
git clone <repository-url>
cd PythonProjects
```

## Usage

### Basic Commands

```bash
# Add a new task
python3 task_tracker.py add "Learn Python programming"

# List all tasks
python3 task_tracker.py list

# List tasks by status
python3 task_tracker.py list --status todo
python3 task_tracker.py list --status in-progress
python3 task_tracker.py list --status done

# Update a task
python3 task_tracker.py update 1 "Master Python programming fundamentals"

# Mark task status
python3 task_tracker.py mark-in-progress 1
python3 task_tracker.py mark-done 1
python3 task_tracker.py mark-todo 1

# Delete a task
python3 task_tracker.py delete 1

# Show help
python3 task_tracker.py --help
```

### Alternative Executable

You can also use the `task-cli` executable:

```bash
./task-cli add "New task"
./task-cli list
```

## Task Status Indicators

- `[ ]` - Todo
- `[~]` - In Progress  
- `[x]` - Done

## Data Storage

Tasks are stored in a `tasks.json` file in the same directory as the script. The file is created automatically when you add your first task.
