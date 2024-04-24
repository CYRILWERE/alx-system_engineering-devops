#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress from a REST API
and exports it to a CSV file.
"""

import requests
import sys
import csv

def fetch_todo_list(employee_id):
    """
    Fetches the TODO list for the given employee ID from the API.
    """
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)
    response = requests.get(url)
    return response.json()

def export_to_csv(employee_id, todo_list):
    """
    Exports the TODO list to a CSV file.
    """
    filename = "{}.csv".format(employee_id)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todo_list:
            writer.writerow([task['userId'], task['username'], task['completed'], task['title']])
    print("Data exported to:", filename)

def main():
    """
    Main function to handle command-line input and output.
    """
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    todo_list = fetch_todo_list(employee_id)
    
    export_to_csv(employee_id, todo_list)

if __name__ == "__main__":
    main()

