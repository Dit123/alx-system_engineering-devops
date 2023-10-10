import requests
import sys

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

            # Calculate the number of completed tasks and the total number of tasks
            num_completed_tasks = len(completed_tasks)
            total_tasks = len(todo_list)

            # Display the employee's TODO list progress
            print(f"Employee {todo_list[0]['name']} is done with tasks ({num_completed_tasks}/{total_tasks}):")

            # Display titles of completed tasks
            for task in completed_tasks:
                print(f"\t{task['title']}")

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

