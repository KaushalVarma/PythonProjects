#!/usr/bin/env python3
"""
Task Tracker CLI - A simple command line interface to track tasks.
"""

import json
import os
import sys
import argparse
from datetime import datetime
from typing import List, Dict, Any


class TaskTracker:
    def __init__(self, data_file: str = "tasks.json"):
        self.data_file = data_file
        self.tasks = self._load_tasks()
    
    def _load_tasks(self) -> List[Dict[str, Any]]:
        """Load tasks from JSON file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                return []
        return []
    
    def _save_tasks(self) -> None:
        """Save tasks to JSON file."""
        with open(self.data_file, 'w') as f:
            json.dump(self.tasks, f, indent=2)
    
    def _get_next_id(self) -> int:
        """Get the next available task ID."""
        if not self.tasks:
            return 1
        return max(task['id'] for task in self.tasks) + 1
    
    def add_task(self, description: str) -> None:
        """Add a new task."""
        task = {
            'id': self._get_next_id(),
            'description': description,
            'status': 'todo',
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        self.tasks.append(task)
        self._save_tasks()
        print(f"Task added successfully (ID: {task['id']})")
    
    def list_tasks(self, status: str = None) -> None:
        """List all tasks or tasks with specific status."""
        filtered_tasks = self.tasks
        if status:
            filtered_tasks = [task for task in self.tasks if task['status'] == status]
        
        if not filtered_tasks:
            status_msg = f" with status '{status}'" if status else ""
            print(f"No tasks found{status_msg}")
            return
        
        for task in filtered_tasks:
            status_indicator = {
                'todo': '[ ]',
                'in-progress': '[~]',
                'done': '[x]'
            }.get(task['status'], '[?]')
            
            print(f"{task['id']}. {status_indicator} {task['description']}")
    
    def update_task(self, task_id: int, description: str) -> None:
        """Update task description."""
        task = self._find_task(task_id)
        if task:
            task['description'] = description
            task['updated_at'] = datetime.now().isoformat()
            self._save_tasks()
            print(f"Task {task_id} updated successfully")
        else:
            print(f"Task with ID {task_id} not found")
    
    def delete_task(self, task_id: int) -> None:
        """Delete a task."""
        task = self._find_task(task_id)
        if task:
            self.tasks.remove(task)
            self._save_tasks()
            print(f"Task {task_id} deleted successfully")
        else:
            print(f"Task with ID {task_id} not found")
    
    def mark_task(self, task_id: int, status: str) -> None:
        """Mark task with specific status."""
        valid_statuses = ['todo', 'in-progress', 'done']
        if status not in valid_statuses:
            print(f"Invalid status. Valid statuses are: {', '.join(valid_statuses)}")
            return
        
        task = self._find_task(task_id)
        if task:
            task['status'] = status
            task['updated_at'] = datetime.now().isoformat()
            self._save_tasks()
            print(f"Task {task_id} marked as {status}")
        else:
            print(f"Task with ID {task_id} not found")
    
    def _find_task(self, task_id: int) -> Dict[str, Any]:
        """Find task by ID."""
        for task in self.tasks:
            if task['id'] == task_id:
                return task
        return None


def main():
    parser = argparse.ArgumentParser(description='Task Tracker CLI')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', help='Task description')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List tasks')
    list_parser.add_argument('--status', choices=['todo', 'in-progress', 'done'], 
                            help='Filter by status')
    
    # Update command
    update_parser = subparsers.add_parser('update', help='Update a task')
    update_parser.add_argument('id', type=int, help='Task ID')
    update_parser.add_argument('description', help='New task description')
    
    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', type=int, help='Task ID')
    
    # Mark commands
    mark_todo_parser = subparsers.add_parser('mark-todo', help='Mark task as todo')
    mark_todo_parser.add_argument('id', type=int, help='Task ID')
    
    mark_progress_parser = subparsers.add_parser('mark-in-progress', help='Mark task as in-progress')
    mark_progress_parser.add_argument('id', type=int, help='Task ID')
    
    mark_done_parser = subparsers.add_parser('mark-done', help='Mark task as done')
    mark_done_parser.add_argument('id', type=int, help='Task ID')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    tracker = TaskTracker()
    
    if args.command == 'add':
        tracker.add_task(args.description)
    elif args.command == 'list':
        tracker.list_tasks(args.status)
    elif args.command == 'update':
        tracker.update_task(args.id, args.description)
    elif args.command == 'delete':
        tracker.delete_task(args.id)
    elif args.command == 'mark-todo':
        tracker.mark_task(args.id, 'todo')
    elif args.command == 'mark-in-progress':
        tracker.mark_task(args.id, 'in-progress')
    elif args.command == 'mark-done':
        tracker.mark_task(args.id, 'done')


if __name__ == '__main__':
    main()