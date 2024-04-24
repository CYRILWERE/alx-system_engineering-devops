#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress from a REST API.
"""

import requests
import sys

def fetch_todo_list(employee_id):
    """
    Fetches the TODO list for the given employee ID from the API.
    """
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)
    response = requests.get(url)
    return response.json()

def main():
    """
    Main function to handle command-line input and output.
    """
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    todo_list = fetch_todo_list(employee_id)

    completed_tasks = [task for task in todo_list if task['completed']]
    total_tasks = len(todo_list)
    num_completed_tasks = len(completed_tasks)
    employee_name = todo_list[0]['username']

    print("Employee {} is done with tasks({}/{}):".format(employee_name, num_completed_tasks, total_tasks))
    for task in completed_tasks:
        print("\t{}".format(task['title']))

if __name__ == "__main__":
    main()

