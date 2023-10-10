#!/usr/bin/python3
import requests
import json
import sys
import os

def fetch_employee_todo_list(employee_id):
    # Define the API URL with the employee ID
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    try:
        # Send an HTTP GET request to the API
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            todo_list = response.json()

            # Filter completed tasks
            completed_tasks = [task for task in todo_list if task['completed']]

            # Create a JSON object with the employee's TODO list progress
            json_data = {
                "USER_ID": [{
                    "task": task['title'],
                    "completed": task['completed'],
                    "username": todo_list[0]['name']
                } for task in completed_tasks]
            }

            # Get the directory of the script
            script_dir = os.path.dirname(os.path.abspath(__file__))

            # Create the JSON file with the data
            json_file_name = os.path.join(script_dir, f'{employee_id}.json')
            with open(json_file_name, 'w') as json_file:
                json.dump(json_data, json_file, indent=4)

            print(f"Data exported to {json_file_name}")

        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_list(employee_id)

