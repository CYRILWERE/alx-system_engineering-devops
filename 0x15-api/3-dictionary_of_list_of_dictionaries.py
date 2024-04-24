#!/usr/bin/python3
"""Export all tasks to JSON"""

import json
import requests
from sys import argv


def export_all_to_json():
    """Export all tasks to JSON"""

    # Fetch data from the API
    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)
    tasks = response.json()

    # Organize tasks by user ID
    tasks_by_user = {}
    for task in tasks:
        user_id = task.get('userId')
        if user_id:
            if user_id not in tasks_by_user:
                tasks_by_user[user_id] = []
            tasks_by_user[user_id].append({
                "username": task.get('username'),
                "task": task.get('title'),
                "completed": task.get('completed')
            })

    # Write tasks to JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(tasks_by_user, json_file)


if __name__ == "__main__":
    export_all_to_json()

