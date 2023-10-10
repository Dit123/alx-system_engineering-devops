#!/usr/bin/python3
import requests
import json

def fetch_all_employee_todo_lists():
    # Define the API URL for all employees' TODO lists
    url = 'https://jsonplaceholder.typicode.com/users'

    try:
        # Send an HTTP GET request to the API to retrieve all users
        response_users = requests.get(url)

        # Check if the request was successful (status code 200)
        if response_users.status_code == 200:
            users = response_users.json()

            # Create a dictionary to store data for all employees
            all_employees_data = {}

            # Loop through each employee
            for user in users:
                user_id = user['id']
                username = user['username']

                # Define the API URL for the employee's TODO list
                todo_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'

                # Send an HTTP GET request to the employee's TODO list
                response_todo = requests.get(todo_url)

                # Check if the request was successful (status code 200)
                if response_todo.status_code == 200:
                    todo_list = response_todo.json()

                    # Create a list to store tasks for this employee
                    employee_tasks = []

                    # Loop through each task and add it to the list
                    for task in todo_list:
                        employee_tasks.append({
                            "username": username,
                            "task": task['title'],
                            "completed": task['completed']
                        })

                    # Add the employee's tasks to the dictionary
                    all_employees_data[user_id] = employee_tasks

            # Create a JSON file with the data for all employees
            json_file_name = 'todo_all_employees.json'
            with open(json_file_name, 'w') as json_file:
                json.dump(all_employees_data, json_file, indent=4)

            print(f"Data exported to {json_file_name}")

        else:
            print(f"Failed to retrieve user data. Status code: {response_users.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_all_employee_todo_lists()

