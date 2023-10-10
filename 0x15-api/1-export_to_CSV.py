import requests
import csv
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

            # Create a CSV file with the employee's TODO list progress
            csv_file_name = f'{employee_id}.csv'
            with open(csv_file_name, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                
                # Write the CSV header
                csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
                
                # Write task data
                for task in completed_tasks:
                    csv_writer.writerow([employee_id, todo_list[0]['name'], "completed", task['title']])

            print(f"Data exported to {csv_file_name}")

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

