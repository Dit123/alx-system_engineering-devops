import json

# Define the JSON structure representing TODO list data
data = {
    "1": [
        {"username": "user1", "task": "Task 1", "completed": True},
        {"username": "user1", "task": "Task 2", "completed": False}
    ],
    "2": [
        {"username": "user2", "task": "Task 3", "completed": True},
        {"username": "user2", "task": "Task 4", "completed": True}
    ],
    "3": [
        {"username": "user3", "task": "Task 5", "completed": False},
        {"username": "user3", "task": "Task 6", "completed": False}
    ]
}

# Write the JSON data to a file
with open('todo_all_employees.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Data exported to todo_all_employees.json")

